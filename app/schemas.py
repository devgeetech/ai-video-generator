from pydantic import BaseModel


class GenerateVideoPayload(BaseModel):
    prompt: str
