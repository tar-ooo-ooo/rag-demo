from typing import Dict

APP_TITLE = "FastAPI Project"

ROOT_MESSAGE = "Hello, FastAPI!"
HEALTH_STATUS = "ok"

USER_NOT_FOUND_MESSAGE = "User not found"

FAKE_USERS: Dict[int, dict] = {
    1: {"id": 1, "name": "Taro"},
    2: {"id": 2, "name": "Yoko"},
}
