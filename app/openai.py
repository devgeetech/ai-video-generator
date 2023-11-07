from openai import OpenAI
from .config import settings
import json

client = OpenAI(api_key=settings.open_ai_api_key)


def get_open_ai_client():
    return client


def get_script(prompt=str):
    res = client.chat.completions.create(
        model="gpt-4-1106-preview",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": "You are an automated system that helps generate 8-second videos. The user will provide a prompt, based on which, you will return a JSON array of objects named script. Each sentence of the script will be an object in the array. The object will have the following attributes. text - the sentence of the script, imagePrompt - a prompt that can be sent to DALL-E to generate the perfect image for the given sentence, that also aligns with the overall context of the video",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )
    json_str = res.choices[0].message.content
    return json.loads(json_str)


def get_image(prompt=str):
    response = client.images.generate(
        model="dall-e-2",
        prompt=prompt,
        size="256x256",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    return image_url
