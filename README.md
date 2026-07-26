# AI Automation Portfolio — Ahmed Basolan

A collection of production n8n workflows I've built for clients and personal projects, covering voice agents, multi-step content generation, lead-gen pipelines, and social media automation. Each folder is a real, working automation — exported directly from n8n, with client-specific identifiers (Sheet/Drive/Calendar IDs, account IDs) replaced with placeholders so the workflow structure and logic are fully visible while no one's actual data ships with it.

## Projects

| Project | What it does | Stack highlights |
|---|---|---|
| [Medical Clinic Voice Agent](./medical-clinic-voice-agent) | Inbound call handling + appointment booking for a dental clinic | OpenAI agent, Google Calendar, Google Sheets |
| [Social Media Content Pipeline](./aaz-social-media-pipeline) | Drive upload → AI caption generation → auto-publish to Instagram/Facebook | Gemini, OpenAI, Facebook Graph API |
| [Lead Gen & Outreach Agent](./lead-gen-outreach-agent) | Maps-sourced leads → email verification → AI-drafted outreach | OpenAI agent + tool-calling, Google Sheets, Gmail |
| [AI Ad Creator](./ai-ad-creator) | Product photo → approved ad concept → generated image/video | OpenAI vision + agent, GPT-Image, Veo3, Telegram |
| [UGC Clip Generator](./ugc-clip-generator) | Product photo → short-form AI-generated UGC-style video clips | OpenAI vision + agent, GPT-Image, Veo3, Telegram |
| [Logo Animation Generator](./logo-animation-generator) | Static logo → animated logo sting, queued via spreadsheet | OpenAI vision + agent, Google Veo, Google Sheets |
| [AI Fitness Coach](./strava-fitness-coach) | Strava activity → personalized coaching feedback via email/WhatsApp | Gemini agent, Strava API, Gmail, WhatsApp Business API |

## How to read these

Each folder contains:
- `workflow.json` — the sanitized n8n export. Importable directly into n8n (Workflows → Import from File) to inspect or run.
- `README.md` — what the workflow does, an architecture diagram, the stack involved, and what needs to be reconfigured (credentials, IDs) to run it yourself.

None of these are toy demos — they were built to run unattended against real accounts and real data. The placeholders exist so you can see exactly how they're wired without needing (or getting) access to anyone's real business accounts.

## About me

I'm an AI Automation Engineer based in Dubai, UAE, building production AI systems — voice agents, multi-step content generation, RAG pipelines, and workflow automation — for real businesses. [LinkedIn](https://linkedin.com/in/ahmed-basolan-80364025a)
