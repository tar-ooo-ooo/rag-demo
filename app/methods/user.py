from typing import Optional

from app.services.user import get_user_from_db


def get_user_profile(user_id: int) -> Optional[dict]:
    user = get_user_from_db(user_id)

    if user is None:
        return None

    return {
        "id": user["id"],
        "name": user["name"],
        "display_name": f"User: {user['name']}",
    }
