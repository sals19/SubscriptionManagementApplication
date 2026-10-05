from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.repositories.subscription_repository import (
    SubscriptionRepository
)
from app.services.subscription_service import SubscriptionService
from app.schemas.subscription import (
    SubscriptionResponse,
    CreateSubscriptionRequest
)


router = APIRouter(
    prefix="/subscriptions",
    tags=["Subscriptions"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def get_service(
    db: Session = Depends(get_db)
):

    repository = SubscriptionRepository(db)

    return SubscriptionService(repository)

@router.get(
    "/{subscription_id}",
    response_model=SubscriptionResponse
)
def get_subscription(
    subscription_id: str,
    service: SubscriptionService = Depends(get_service)
):

    try:

        subscription = service.get_subscription(
            subscription_id
        )

        return SubscriptionResponse(
            subscription_id=subscription.subscription_id.hex(),
            subscription_name=subscription.subscription_name,
            subscription_type=subscription.subscription_type,
            user_id=subscription.user_id.hex(),
            plan_id=subscription.plan_id,
            status=subscription.status,
            start_date=subscription.start_date.isoformat(),
            end_date=(
                subscription.end_date.isoformat()
                if subscription.end_date
                else None
            )
        )

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

@router.get(
    "/user/{user_id}",
    response_model=SubscriptionResponse
)
def get_user_subscription(
    user_id: str,
    service: SubscriptionService = Depends(get_service)
):

    try:

        subscription = service.get_user_subscription(
            user_id
        )

        return SubscriptionResponse(
            subscription_id=subscription.subscription_id.hex(),
            subscription_name=subscription.subscription_name,
            subscription_type=subscription.subscription_type,
            user_id=subscription.user_id.hex(),
            plan_id=subscription.plan_id,
            status=subscription.status,
            start_date=subscription.start_date.isoformat(),
            end_date=(
                subscription.end_date.isoformat()
                if subscription.end_date
                else None
            )
        )

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

@router.post(
    "",
    response_model=SubscriptionResponse,
    status_code=201
)
def create_subscription(
    request: CreateSubscriptionRequest,
    service: SubscriptionService = Depends(get_service)
):

    try:

        subscription = service.create_subscription(
            user_id=request.user_id,
            plan_id=request.plan_id,
            subscription_name=request.subscription_name,
            subscription_type=request.subscription_type
        )

        return SubscriptionResponse(
            subscription_id=subscription.subscription_id.hex(),
            subscription_name=subscription.subscription_name,
            subscription_type=subscription.subscription_type,
            user_id=subscription.user_id.hex(),
            plan_id=subscription.plan_id,
            status=subscription.status,
            start_date=subscription.start_date.isoformat(),
            end_date=(
                subscription.end_date.isoformat()
                if subscription.end_date
                else None
            )
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

