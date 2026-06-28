from app.routers import user_router
from fastapi import FastAPI

app = FastAPI(title="FastAPI Project")

app.include_router(user_router)

@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello, FastAPI!"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
