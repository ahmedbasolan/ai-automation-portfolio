# Social Media Content Pipeline (Google Drive to Instagram/Facebook)

Built for AAZ Jewellery. Drops a photo or video into a watched Google Drive folder and the workflow analyzes it, writes on-brand hook-style caption copy, and publishes it to both Instagram and Facebook automatically — no manual posting.

## What it replaces

A person manually reviewing new product photos/videos, writing captions, and posting them one by one across two platforms.

## Architecture

```
Google Drive Trigger (new file in watched folder)
        |
        v
Download file --> Analyze image/video (Gemini, multimodal)
        |
        v
   AI Agent (OpenAI, with a "Think" tool + structured output parser)
   writes platform-ready caption/hook copy
        |
        v
     Switch (image vs. video)
    /                        \
Instagram container flow   Facebook container flow
(create container -> wait -> publish)   (create container -> wait -> publish)
```

Media type determines the path: images go through one container-creation flow, videos go through a separate one with a wait step (Instagram/Facebook require processing time for video containers before they can be published), then both post through the Facebook Graph API.

## Stack

- n8n (orchestration)
- Google Drive (trigger + file download)
- Google Gemini (multimodal image/video analysis)
- OpenAI (caption/hook generation via LangChain agent, structured output)
- Cloudinary (hosts each file at a public URL, which the Graph API needs to fetch the media)
- Facebook Graph API (Instagram + Facebook publishing)

## Notes on this repo

Sanitized of the original Drive folder ID, the real Instagram Business/Facebook Page IDs and the Cloudinary account. Replace `YOUR_DRIVE_FOLDER_ID`, `YOUR_INSTAGRAM_BUSINESS_ID`, `YOUR_FACEBOOK_PAGE_ID`, `YOUR_CLOUDINARY_CLOUD_NAME` and `YOUR_UNSIGNED_UPLOAD_PRESET` with your own before running it, and connect your own Google/Meta/OpenAI credentials.

An unsigned upload preset accepts uploads from anyone who knows the cloud name and preset name, so keep both out of anything public, or restrict the preset in Cloudinary (allowed formats, size limit, folder).
