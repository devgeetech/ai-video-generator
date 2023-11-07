from fastapi import FastAPI
from .openai import get_script, get_image
from .murf import get_voiceover_url
from .moviepy import get_final_video

app = FastAPI()


@app.get("/")
def get_root():
    return {"message": "Hello World"}


# @app.get("/comp")
# def get_comp():
#     res = get_script("Documentary on sahara desert")
#     return {"data": res}


# @app.get("/img")
# def get_img():
#     res = get_image("Tuareg nomads traveling across the Sahara Desert")
#     return {"data": res}


# @app.get("/voice")
# def get_voice():
#     res = get_voiceover_url(
#         "Dive into the deep blue and discover the world of dolphins.", "en-US-carter"
#     )
#     return {"data": res}


# @app.get("/video")
# def get_video():
#     data_list = [
#         {
#             "audioUrl": "https://murf.ai/user-upload/one-day-temp/ca5501df-3d77-43a3-9d03-6eb99368cc0b.wav?response-cache-control=max-age%3D604801&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231107T000000Z&X-Amz-SignedHeaders=host&X-Amz-Expires=259200&X-Amz-Credential=AKIA27M5532DYKBCJICE%2F20231107%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Signature=1d2610c22177d63659a8ad76489621857ae39973aa3acef1dc2a1ebf6351eea5",
#             "imageUrl": "https://i.imgur.com/mCgVt5r.png",
#         },
#         {
#             "audioUrl": "https://murf.ai/user-upload/one-day-temp/4778aea1-d754-4cdb-ae8d-92c525995146.wav?response-cache-control=max-age%3D604801&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231107T000000Z&X-Amz-SignedHeaders=host&X-Amz-Expires=259200&X-Amz-Credential=AKIA27M5532DYKBCJICE%2F20231107%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Signature=1e654e1895b1193455ac3b21a29c80cb52bcdbd22017742b24d087b774ede29e",
#             "imageUrl": "https://i.imgur.com/mCgVt5r.png",
#         },
#         {
#             "audioUrl": "https://murf.ai/user-upload/one-day-temp/dd05a67b-c124-46eb-9d63-9cfa602c4437.wav?response-cache-control=max-age%3D604801&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231107T000000Z&X-Amz-SignedHeaders=host&X-Amz-Expires=259200&X-Amz-Credential=AKIA27M5532DYKBCJICE%2F20231107%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Signature=dd28189de73f0c30a72fbb31d6d23a477a1d0b7789ebfdff759bd496a1e1b405",
#             "imageUrl": "https://i.imgur.com/mCgVt5r.png",
#         },
#     ]

#     res = get_final_video(data_list)
#     return {"message": "success"}


@app.get("/ai-video")
def get_ai_video():
    # generate script first
    script = get_script("Documentary on the penguins of antarctica")
    script_arr = script["script"]

    data_list = []

    # go through each item in script_arr and generate image and audio
    for item in script_arr:
        # generate image
        image_url = get_image(item["imagePrompt"])
        # generate audio
        audio_url = get_voiceover_url(item["text"], item["voiceId"])
        # append to url_arr
        data_list.append({"imageUrl": image_url, "audioUrl": audio_url})

    res = get_final_video(data_list)
    return {"message": "success"}
