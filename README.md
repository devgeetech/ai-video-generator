## Steps

1. `pip install "fastapi[all]"`
2. `pip install openai`
3. Set up `.env` and `config.py`
4. Setting up openai config
5. Setting up prompt to generate script and image prompts
6. Set up Murf for voiceover generation
7. `pip install moviepy`

## Voices to use

Documentaries: en-UK-gabriel
Promo: en-UK-reggie, en-US-caleb
Informational: en-UK-hazel
General & Narration: en-US-miles

## Sample script

```json
{
  "data": {
    "script": [
      {
        "text": "The Sahara Desert, a vast sea of sand, whispers the secrets of a millennia.",
        "imagePrompt": "Endless golden sands of the Sahara Desert under a clear blue sky",
        "voiceId": "en-UK-gabriel"
      },
      {
        "text": "Its dunes, shaped by relentless winds, tell tales of ancient caravans.",
        "imagePrompt": "Wind-sculpted sand dunes in the Sahara Desert with trails left by a caravan",
        "voiceId": "en-UK-gabriel"
      },
      {
        "text": "Once a fertile oasis, the Sahara's climate shift transformed it into an arid wonderland.",
        "imagePrompt": "Historical transition illustration of a fertile Sahara oasis becoming a desert",
        "voiceId": "en-UK-gabriel"
      },
      {
        "text": "Only the hardiest of lives, like the Tuareg nomads, dare call it home.",
        "imagePrompt": "Tuareg nomads traveling across the Sahara Desert",
        "voiceId": "en-UK-gabriel"
      }
    ]
  }
}
```
