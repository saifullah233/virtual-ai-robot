from sqlalchemy.orm import Session

from app.api.users.schemas import UserEnrollRequest
from app.models.user import User


def enroll_user(db: Session, user_data: UserEnrollRequest) -> User:
    user = User(
        name=user_data.name,
        user_type=user_data.user_type,
        college_en=user_data.college_en,
    )
    db.add(user)
    try:
        db.commit()
        db.refresh(user)
    except Exception:
        db.rollback()
        raise
    return user