import requests
from moviepy.editor import (
    ImageClip,
    AudioFileClip,
    concatenate_videoclips,
)
from fastapi.responses import FileResponse


def download_file(url, local_filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename


def get_final_video(data_list):
    video_clips = []
    counter = 0

    for data in data_list:
        audio_url = data["audioUrl"]
        image_url = data["imageUrl"]

        image_path = download_file(image_url, f"image_{counter}.png")
        audio_path = download_file(audio_url, f"audio_{counter}.wav")

        audio_clip = AudioFileClip(audio_path)

        video_clip = ImageClip(image_path, duration=(int(audio_clip.duration) + 1))

        video_clip = video_clip.set_audio(audio_clip)

        video_clips.append(video_clip)

        counter += 1

    final_video = concatenate_videoclips(video_clips)

    output_path = "output_video.mp4"
    final_video.write_videofile(output_path, fps=24, codec="libx264")

    final_video.close()
    return FileResponse(output_path, media_type="video/mp4")
