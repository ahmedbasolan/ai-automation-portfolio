# UGC Clip Generator (Telegram-Operated)

A Telegram-driven pipeline that turns a product photo into short, UGC-style video clips using AI image and video generation — built for fast-turnaround social ad content without booking a shoot.

## What it replaces

Hiring a creator or running a UGC shoot for every product variant/campaign, when a scroll-stopping short clip could be generated directly from a product photo instead.

## Architecture

```
Telegram Trigger (photo sent to bot)
        |
        v
Get image -> Analyze image (OpenAI vision)
        |
        v
Initial Prompt AI Agent (OpenAI + "Think" tool + structured output)
   -> generates image/video prompt variants
        |
        v
Create + poll GPT-Image  /  Create + poll Veo3 (video)
        |
        v
Aggregate outputs -> Telegram: deliver finished clip(s)
```

Similar creative-pipeline shape to the Ad Creator workflow, tuned specifically for short-form UGC-style clips rather than single polished ad assets.

## Stack

- n8n (orchestration)
- Telegram (control interface)
- OpenAI (vision analysis, prompt-generation agent, GPT-Image)
- Google Veo3 (AI video generation, polled asynchronously)

## Notes on this repo

Telegram chat references are resolved at runtime via expressions, not static values. The Telegram bot token itself has been replaced with a placeholder (`YOUR_TELEGRAM_BOT_TOKEN`) — you'll need your own bot token and OpenAI/Veo3 credentials to run it.
