"""Fail if any workflow export carries data that should not be public.

Checks every */workflow.json: it parses, has no pinned execution data, no n8n
instance ID, no credential IDs (names are fine: they tell you what to connect),
and no string that looks like a live secret. Run: python scripts/check_sanitized.py
"""

import json
import re
import sys
from pathlib import Path

SECRET_PATTERNS = {
    "Telegram bot token": r"\b\d{8,10}:[A-Za-z0-9_-]{35}\b",
    "OpenAI key": r"\bsk-[A-Za-z0-9_-]{20,}",
    "Google API key": r"\bAIza[0-9A-Za-z_-]{35}\b",
    "Meta access token": r"\bEAA[A-Za-z0-9]{30,}",
    "Slack token": r"\bxox[abpr]-[A-Za-z0-9-]{10,}",
    "bearer token": r"Bearer\s+[A-Za-z0-9._-]{20,}",
    # A real Cloudinary cloud name next to an unsigned preset lets anyone upload.
    "Cloudinary cloud name": r"api\.cloudinary\.com/v1_1/(?!YOUR_)[A-Za-z0-9_-]+",
}


def problems(path: Path) -> list[str]:
    try:
        wf = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"not valid JSON: {e}"]
    found = []
    if wf.get("pinData"):
        found.append("pinData holds execution data")
    if (wf.get("meta") or {}).get("instanceId"):
        found.append("meta.instanceId is set")
    for node in wf.get("nodes", []):
        for ctype, cred in (node.get("credentials") or {}).items():
            if "id" in cred:
                found.append(f"credential id on '{node['name']}' ({ctype})")
    raw = json.dumps(wf)
    for label, pattern in SECRET_PATTERNS.items():
        if re.search(pattern, raw):
            found.append(f"looks like a {label}")
    return found


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    files = sorted(root.glob("*/workflow.json"))
    failed = False
    for path in files:
        issues = problems(path)
        rel = path.relative_to(root).as_posix()
        print(f"{'FAIL' if issues else 'ok  '} {rel}")
        for issue in issues:
            print(f"       - {issue}")
        failed |= bool(issues)
    if not files:
        print("no */workflow.json found")
        return 1
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
