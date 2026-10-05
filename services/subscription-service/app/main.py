from fastapi import FastAPI

from app.api.subscription_api import router as subscription_router


app = FastAPI(
    title="Subscription Service",
    version="1.0.0"
)


app.include_router(subscription_router)


@app.get("/health")
def health_check():

    return {
        "status": "UP"
    }