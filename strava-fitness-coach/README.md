# AI Fitness Coach (Strava-Triggered)

Watches for new Strava activities and automatically sends a personalized coaching write-up — analysis of the workout plus feedback/encouragement — by email and WhatsApp, without a human coach reviewing every session.

## What it replaces

A coach manually reviewing each logged workout and writing individual feedback, which doesn't scale past a handful of clients.

## Architecture

```
Strava Trigger (new activity logged)
        |
        v
Combine activity data (Code node)
        |
        v
Fitness Coach Agent (Google Gemini, conversational agent)
   analyzes the activity and writes coaching feedback
        |
        v
Structure output -> Convert to HTML
        |
        v
   Send Email                Send WhatsApp message
   (Gmail)                   (WhatsApp Business Cloud API)
```

## Stack

- n8n (orchestration)
- Strava API (activity trigger/data)
- Google Gemini (LangChain conversational agent for coaching analysis)
- Gmail + WhatsApp Business Cloud API (dual-channel delivery)

## Notes on this repo

Sanitized of a real hardcoded recipient email address that was present in the original export — replace `your-email@example.com` with your own, and connect your own Strava/Gemini/Gmail/WhatsApp credentials.
