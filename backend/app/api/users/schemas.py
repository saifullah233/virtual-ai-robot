import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from app.models.user import UserType


class UserEnrollRequest(BaseModel):
    name: str = Field(min_length=1)
    user_type: UserType
    college_en: str | None = None


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    name: str
    user_type: UserType
    college_en: str | None
    memory_enabled: bool
    created_at: datetime
    updated_at: datetime