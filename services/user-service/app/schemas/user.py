from pydantic import BaseModel


class UserResponse(BaseModel):

    user_id: str
    first_name: str
    last_name: str
    email: str