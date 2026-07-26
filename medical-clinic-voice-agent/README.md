# Medical Clinic Voice Agent

An automated inbound-call handling system built for a dental clinic. Callers speak to a voice agent (paired with a speech layer such as ElevenLabs/Twilio in front of this workflow) that checks real appointment availability, books a slot, and logs the patient's details — with zero staff involvement for routine bookings.

## What it replaces

Front-desk staff manually answering every call to check the calendar, take down patient details, and confirm appointments by hand.

## Architecture

```
Caller -> [Voice layer: STT/TTS, not in this repo] -> Webhook Trigger
                                                          |
                                                          v
                                                 Conversational Agent
                                            (LLM: OpenAI, short-term memory)
                                             |             |            |
                                     get_availability  create_appointment  log_patient_details
                                     (Google Calendar)  (Google Calendar)   (Google Sheets)
                                                          |
                                                          v
                                                  Respond to Webhook
```

The agent is a single LLM-driven conversational agent (`dental_agent`) with three callable tools and a sliding-window memory buffer so it can hold a multi-turn conversation (confirm a time, ask a follow-up, handle a change of mind) without losing context mid-call.

## Stack

- n8n (workflow orchestration)
- OpenAI (LLM reasoning via LangChain agent node)
- Google Calendar API (availability + booking, exposed to the agent as callable tools)
- Google Sheets (patient detail logging: name, insurance provider, questions/concerns, timestamps)
- Webhook trigger/response (the integration point for the voice layer)

## Notes on this repo

This is the exported n8n workflow definition (`workflow.json`), sanitized of the original client's live webhook path, Google Sheet ID, and Calendar ID. To run it yourself, replace the placeholder values (`YOUR_WEBHOOK_PATH`, `YOUR_GOOGLE_SHEET_ID`, `your_calendar_id@group.calendar.google.com`) with your own, and connect your own Google/OpenAI credentials in n8n.

This workflow was originally built for a dental practice; the same pattern generalizes to any appointment-based business (clinics, salons, repair services) where availability lives in a calendar and bookings need to happen without a human answering the phone.
