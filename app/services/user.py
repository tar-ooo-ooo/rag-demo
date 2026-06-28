from typing import Optional


def get_user_from_db(user_id: int) -> Optional[dict]:
    fake_bd = {
        1: {"id": 1, "name": "Taro"},
        2: {"id": 2, "name": "Yoko"},
    }

    return fake_bd.get(user_id)
