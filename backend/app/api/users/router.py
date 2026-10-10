from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.users.schemas import UserEnrollRequest, UserResponse
from app.core.database import get_db
from app.services.user_service import enroll_user


router = APIRouter(prefix="/api/v1/users", tags=["users"])


@router.post("/enroll", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def enroll(user_data: UserEnrollRequest, db: Session = Depends(get_db)) -> UserResponse:
    return enroll_user(db, user_data)