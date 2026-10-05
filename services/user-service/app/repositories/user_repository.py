from app.models.user import User


class UserRepository:

    def __init__(self, session):
        self.session = session

    def get_by_id(self, user_id):
        return (
            self.session.query(User)
            .filter(User.user_id == user_id)
            .first()
        )