from typing import Optional

from pydantic import BaseModel


class SubscriptionResponse(BaseModel):

    subscription_id: str
    subscription_name: Optional[str] = None
    subscription_type: Optional[str] = None
    user_id: str
    plan_id: int
    status: str
    start_date: str
    end_date: Optional[str] = None

class CreateSubscriptionRequest(BaseModel):

    user_id: str
    plan_id: int
    subscription_name: str
    subscription_type: str