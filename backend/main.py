from fastapi import FastAPI

from app.api.users.router import router as users_router

app = FastAPI(
    title="Virtual AI Robot",
    description="Interactive AI Robot with Vision, Memory and Context Awareness",
    version="0.1.0"
)

app.include_router(users_router)


@app.get("/")
def root():
    return {
        "project": "Virtual AI Robot",
        "status": "online"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }