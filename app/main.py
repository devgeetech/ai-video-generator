from fastapi import FastAPI
from .openai import get_script, get_image

app = FastAPI()


@app.get("/")
def get_root():
    return {"message": "Hello World"}


@app.get("/comp")
def get_comp():
    res = get_script()
    return {"data": res}


@app.get("/img")
def get_img():
    res = get_image(
        "An over-shoulder shot of a diver observing dolphins in their natural habitat"
    )
    return {"data": res}
