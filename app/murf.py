import requests
import json
from .config import settings


def get_voiceover_url(text=str, voice_id=str):
    url = "https://api.murf.ai/v1/speech/generate-with-key"
    payload = json.dumps(
        {
            "voiceId": voice_id,
            "text": text,
        }
    )
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "api-key": settings.murf_ai_api_key,
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()["audioFile"]
