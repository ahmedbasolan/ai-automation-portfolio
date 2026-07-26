# AI Ad Creator (Telegram-Operated, Human-in-the-Loop)

A Telegram bot that turns a product photo into a finished ad — image or video — using a multi-step AI creative pipeline with a human approval gate before anything renders. Send a photo, get back an on-brand ad concept to approve, then a generated image or Veo3-generated video.

## What it replaces

Briefing a designer/video editor, waiting on drafts, and going back and forth over revisions — compressed into a chat-based approve/regenerate loop you can run from your phone.

## Architecture

```
Telegram Trigger (photo sent to bot)
        |
        v
Get image -> Analyze image (OpenAI vision)
        |
        v
Initial Prompt AI Agent (OpenAI + "Think" tool + structured output)
   generates a creative concept + revised prompt
        |
        v
Telegram: send concept for approval  --[rejected]--> Revised Prompt AI Agent (regenerate)
        |
     [approved]
        |
        v
   If image path:                    If video path:
   Create + poll GPT-Image            Create + poll Veo3 (async, polled via wait loop)
        |                                    |
        v                                    v
   Telegram: send finished photo      Telegram: send finished video
```

The approval step matters: nothing renders (which costs time and generation credits) until a human confirms the creative direction in chat.

## Stack

- n8n (orchestration)
- Telegram (control interface — trigger, approval prompts, delivery)
- OpenAI (vision analysis, creative-direction agent, GPT-Image generation)
- Google Veo3 (AI video generation, polled asynchronously)

## Notes on this repo

Telegram chat references are resolved at runtime via expressions, not static values. The original export did have a live Telegram bot token hardcoded directly into a couple of URLs — that's been replaced with `YOUR_TELEGRAM_BOT_TOKEN`. You'll need your own Telegram bot token and OpenAI/Veo3 credentials configured in n8n to run it.
