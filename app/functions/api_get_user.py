from typing import Optional

from fastapi import HTTPException

from app.config import USER_NOT_FOUND_MESSAGE
from app.methods.user import get_user_profile


def api_get_user(user_id: int) -> Optional[dict]:
    user = get_user_profile(user_id)

    if user is None:
        raise HTTPException(status_code=404, detail=USER_NOT_FOUND_MESSAGE)

    return {
        "success": True,
        "data": user,
    }
