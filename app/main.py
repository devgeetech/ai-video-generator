from fastapi import FastAPI
from .openai import get_script, get_image
from .murf import get_voiceover_url
from .moviepy import get_final_video
from . import schemas

app = FastAPI()


@app.get("/")
def get_root():
    return {"message": "Hello World"}


@app.get("/generate-video")
def get_ai_video(payload: schemas.GenerateVideoPayload):
    script = get_script(prompt=payload.prompt)
    script_arr = script["script"]

    data_list = []

    for item in script_arr:
        image_url = get_image(item["imagePrompt"])
        audio_url = get_voiceover_url(item["text"], item["voiceId"])
        data_list.append({"imageUrl": image_url, "audioUrl": audio_url})

    res = get_final_video(data_list)
    return res
