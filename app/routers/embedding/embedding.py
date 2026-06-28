from app.functions.embedding.api_embedding import api_embedding
from app.schemas.embedding import EmbeddingRequest
from fastapi import APIRouter


embedding_router = APIRouter(prefix="/embedding", tags=["embedding"])


@embedding_router.post("/")
def embedding(body: EmbeddingRequest) -> dict:
    return api_embedding(body)
