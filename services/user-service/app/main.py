from fastapi import FastAPI
from app.api.user_api import router as user_router

app = FastAPI(title="User Service", version="2.0.0")

app.include_router(user_router)

@app.get("/health")
def health_check():
    return {
        "status": "UP"
    }