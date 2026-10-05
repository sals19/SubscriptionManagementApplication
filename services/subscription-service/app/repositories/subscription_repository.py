import uuid
from datetime import date

from app.models.subscription import Subscription


class SubscriptionRepository:

    def __init__(self, session):
        self.session = session

    def get_by_id(self, subscription_id):

        return (
            self.session.query(Subscription)
            .filter(
                Subscription.subscription_id == subscription_id
            )
            .first()
        )

    def get_by_user_id(self, user_id):

        return (
            self.session.query(Subscription)
            .filter(
                Subscription.user_id == user_id
            )
            .first()
        )

    def create_subscription(
        self,
        user_id,
        plan_id,
        subscription_name,
        subscription_type
    ):

        subscription = Subscription()

        subscription.subscription_id = uuid.uuid4().bytes
        subscription.user_id = user_id
        subscription.plan_id = plan_id
        subscription.subscription_name = subscription_name
        subscription.subscription_type = subscription_type

        subscription.start_date = date.today()
        subscription.status = "ACTIVE"

        self.session.add(subscription)

        self.session.commit()

        self.session.refresh(subscription)

        return subscription