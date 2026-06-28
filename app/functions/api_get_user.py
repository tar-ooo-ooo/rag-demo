from typing import Optional

from fastapi import HTTPException

from app.methods.user import get_user_profile


def api_get_user(user_id: int) -> Optional[dict]:
    user = get_user_profile(user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "success": True,
        "data": user,
    }
