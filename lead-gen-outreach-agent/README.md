# Lead Gen & Outreach Agent (Google Maps → Verified Email → AI-Drafted Follow-Up)

Takes a list of business leads (sourced via a Google Maps scraper feeding into Google Sheets), deduplicates and validates them, finds and verifies a real contact email per domain, and hands off to an AI agent that drafts a personalized outreach email — ready for review in Gmail rather than auto-sent blind.

## What it replaces

Manually scrolling through Google Maps results, guessing at contact emails, and writing outreach messages one lead at a time.

## Architecture

```
Google Sheets Trigger (new leads appended by an upstream Maps scraper)
        |
        v
Remove duplicates -> Filter (has website?) -> Extract domain
        |
        v
Get URL data (HTTP) -> Find domain emails -> Filter bad/invalid emails -> Lowercase/normalize
        |
        v
Append verified lead to sheet
        |
        v
   AI Agent (OpenAI + "Think" tool + short-term memory)
   drafts a personalized outreach message per lead
        |
        v
   Gmail: create draft (human reviews and sends — not auto-sent)
```

**Architecture note, stated plainly:** this is a single AI agent with tool-calling (a "Think" step and short-term memory), orchestrating a multi-stage data pipeline — not multiple coordinating agents. The intelligence is concentrated in one agent node; everything upstream (dedup, domain/email extraction, validation) is deterministic n8n logic, not separate agents. Described that way here on purpose, so the architecture matches what's actually in `workflow.json`.

## Stack

- n8n (orchestration, batching/looping over large lead lists)
- Google Sheets (lead intake and storage)
- HTTP Request nodes + custom code (domain/email extraction and validation)
- OpenAI (LangChain agent for outreach drafting)
- Gmail (draft creation for human review)

## Notes on this repo

Sanitized of the original Google Sheet ID — replace `YOUR_GOOGLE_SHEET_ID` with your own, and connect your own Google/OpenAI credentials.
