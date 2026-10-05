class UserService:

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def get_user(self, user_id: str):

        if isinstance(user_id, str):
            user_id = bytes.fromhex(user_id)

        user = self.user_repository.get_by_id(user_id)

        if not user:
            raise ValueError("User not found")

        return user