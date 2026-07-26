# Logo Animation Generator

Feeds a static logo (queued via Google Sheets) through an AI creative-direction agent and Google Veo, turning a flat brand asset into a short animated logo sting — batch-processable from a spreadsheet queue instead of one-off manual requests.

## What it replaces

Commissioning a motion designer for a simple animated logo treatment, or manually prompting/regenerating video-gen tools one logo at a time.

## Architecture

```
Get input logo (row from Google Sheets queue)
        |
        v
Analyze image (OpenAI vision) -> Initial Prompt AI Agent
   (OpenAI + "Think" tool + structured output)
   generates creative direction for the animation
        |
        v
Create + poll Veo (async, polled via wait loop)
        |
        v
Update row in sheet (status + output link)
```

Sheet-driven rather than chat-driven: rows represent a queue, and the workflow processes each logo, writing status and output back to the same sheet — a batch-processing pattern rather than a single interactive session.

## Stack

- n8n (orchestration)
- Google Sheets (job queue + status/output tracking)
- OpenAI (vision analysis + creative-direction agent)
- Google Veo (AI video generation)

## Notes on this repo

Sanitized of the original Google Sheet ID, and of a real brand name that was hardcoded into an example creative-direction payload (replaced with a generic "Example Brand" placeholder). Replace `YOUR_GOOGLE_SHEET_ID` with your own, and connect your own Google/OpenAI/Veo credentials.
