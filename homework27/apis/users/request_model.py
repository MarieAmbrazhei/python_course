"""Module contains Pydantic models."""
from typing import Optional
from pydantic import BaseModel, Field, conint, field_validator

ARBITRARY_TYPES_ALLOWED = True


class UserRequestModel(BaseModel):
    """
    Pydantic model for creating a new user request.
    """
    name: str = Field(..., min_length=3)
    email: str = Field(..., pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    age: int = Field(ge=18, le=120)
    phoneNumber: str = Field(..., pattern=r'^\+\d{7,10}$')
    address: str = Field(..., min_length=10)
    role: Optional[str] = Field(None, max_length=20)
    referralCode: Optional[str] = Field(None, min_length=8, max_length=8)


class UserUpdateRequestModel(BaseModel):
    """
    Pydantic model for updating an existing user request.
    """
    name: str = Field(..., min_length=3)
    email: str = Field(..., pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    age: conint(ge=18, le=120)
    phoneNumber: str = Field(..., pattern=r'^\+\d{7,10}$')
    address: str = Field(..., min_length=10)
    role: Optional[str] = Field(None, max_length=20)
    referralCode: Optional[str] = Field(None, min_length=8, max_length=8)

    @field_validator('role')
    @classmethod
    def validate_role(cls, v):
        """
        Validates the role field to ensure it is one of the allowed values.
        """
        if v and v not in ["user", "admin", "moderator"]:
            raise ValueError('Role must be one of "user", "admin", or "moderator"')
        return v
