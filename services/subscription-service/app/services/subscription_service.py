class SubscriptionService:

    def __init__(self, subscription_repository):
        self.subscription_repository = subscription_repository

    def get_subscription(self, subscription_id: str):

        if isinstance(subscription_id, str):
            subscription_id = bytes.fromhex(subscription_id)

        subscription = (
            self.subscription_repository
            .get_by_id(subscription_id)
        )

        if not subscription:
            raise ValueError("Subscription not found")

        return subscription

    def get_user_subscription(self, user_id: str):

        if isinstance(user_id, str):
            user_id = bytes.fromhex(user_id)

        subscription = (
            self.subscription_repository
            .get_by_user_id(user_id)
        )

        if not subscription:
            raise ValueError("Subscription not found")

        return subscription

    def create_subscription(
        self,
        user_id: str,
        plan_id: int,
        subscription_name: str,
        subscription_type: str
    ):

        if isinstance(user_id, str):
            user_id = bytes.fromhex(user_id)

        return self.subscription_repository.create_subscription(
            user_id=user_id,
            plan_id=plan_id,
            subscription_name=subscription_name,
            subscription_type=subscription_type
        )