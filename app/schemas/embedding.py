from pydantic import BaseModel


class EmbeddingRequest(BaseModel):
    context: str
