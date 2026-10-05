from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService
from app.schemas.user import UserResponse

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get(
    "/{user_id}",
    response_model=UserResponse
)
def get_user(
    user_id: str,
    db: Session = Depends(get_db)):
    try:
        repository = UserRepository(db)
        service = UserService(repository)
        user = service.get_user(user_id)
        return UserResponse(user_id=user.user_id.hex(),
                            first_name=user.first_name,
                            last_name=user.last_name,
                            email=user.email)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
