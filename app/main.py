from app.config import APP_TITLE, HEALTH_STATUS, ROOT_MESSAGE
from app.routers import user_router
from fastapi import FastAPI

app = FastAPI(title=APP_TITLE)

app.include_router(user_router)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": ROOT_MESSAGE}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": HEALTH_STATUS}
