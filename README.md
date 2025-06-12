# AI Fact Checker (Flask + Gemini API)

This Flask app verifies facts using Google's Gemini API.

## Run Locally

```bash

https://transcendent-sable-22da4c.netlify.app/

```

## Endpoints

### POST `/verify`

**Request Body:**
```json
{
  "query": "India is the largest democracy in the world."
}
```

**Response:**
```json
{
  "result": "✅ True. India is..."
}
```

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

## Deploy on Vercel

```bash
vercel
```
