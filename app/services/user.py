from typing import Optional

from app.config import FAKE_USERS


def get_user_from_db(user_id: int) -> Optional[dict]:
    return FAKE_USERS.get(user_id)
