from app.functions.api_get_user import api_get_user
from fastapi import APIRouter

user_router = APIRouter(prefix="/user", tags=["user"])


@user_router.get("/{user_id}")
def get_user(user_id: int) -> dict:
    return api_get_user(user_id)
