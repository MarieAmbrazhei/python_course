from typing import Optional, List
import datetime
from pydantic import BaseModel, Field, conint, ConfigDict


class BaseConfigModel(BaseModel):
    """
    Base configuration model for all Pydantic models in this module.
    This configuration allows arbitrary types for fields.
    """
    model_config = ConfigDict(arbitrary_types_allowed=True)


class UserResponseModel(BaseConfigModel):
    """
    Model for user response data.
    """
    id: str = Field(..., min_length=1)
    name: str = Field(..., min_length=3)
    email: Field(..., pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    age: conint(ge=18, le=120)
    phoneNumber: Field(..., pattern=r'^\+\d{7,10}$')
    address: str = Field(..., min_length=10)
    role: Optional[str] = Field(None, max_length=20)
    referralCode: Optional[str] = Field(None, min_length=8, max_length=8)
    status: Optional[str] = Field(None, max_length=20)


class UserGetResponseModel(BaseConfigModel):
    """
    Model for user data retrieval response.
    """
    id: str = Field(..., min_length=1)
    name: str = Field(..., min_length=3)
    email: Field(..., pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    age: conint(ge=18, le=120)
    phoneNumber: Field(..., pattern=r'^\+\d{7,10}$')
    address: str = Field(..., min_length=10)
    role: Optional[str] = Field(None, max_length=20)
    referralCode: Optional[str] = Field(None, min_length=8, max_length=8)
    createdAt: datetime = Field(..., description="Timestamp of user creation")
    createdBy: str = Field(..., description="ID of the user who created this entry")


class UserUpdateResponseModel(BaseConfigModel):
    """
    Model for user update response data.
    """
    id: str = Field(..., min_length=1)
    name: str = Field(..., min_length=3)
    email: Field(..., pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    age: conint(ge=18, le=120)
    phoneNumber: Field(..., pattern=r'^\+\d{7,10}$')
    address: str = Field(..., min_length=10)
    role: Optional[str] = Field(None, max_length=20)
    referralCode: Optional[str] = Field(None, min_length=8, max_length=8)
    status: Optional[str] = Field(None, max_length=20)


class UserDeleteResponseModel(BaseConfigModel):
    """
    Model for user deletion response data.
    """
    id: str = Field(..., min_length=1)
    status: Optional[str] = Field(None, max_length=20)


class UserStatusCheckResponseModel(BaseConfigModel):
    """
    Model for checking user status.
    """
    id: str = Field(..., min_length=1)
    name: str = Field(..., min_length=3)
    email: Field(..., pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    createdAt: datetime = Field(..., description="Timestamp of user creation")
    createdBy: str = Field(..., description="ID of the user who created this entry")
    status: Optional[str] = Field(None, max_length=20)


class UsersGetModel(BaseConfigModel):
    """
    Model for individual user data retrieval.
    """
    id: str = Field(..., min_length=1, alias='_id')
    name: str = Field(..., min_length=3)
    email: str = Field(..., pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    age: Optional[conint(ge=18, le=120)] = None
    phoneNumber: Optional[str] = Field(None, pattern=r'^\+\d{7,10}$')
    address: Optional[str] = Field(None, min_length=10)
    role: Optional[str] = Field(None, max_length=20)
    referralCode: Optional[str] = Field(None, min_length=8, max_length=8)
    createdAt: datetime = Field(..., description="Timestamp of user creation")
    createdBy: int = Field(..., description="ID of the user who created this entry")
    status: Optional[str] = Field(None, max_length=20)


class UsersGetResponseModel(BaseConfigModel):
    """
    Model for paginated list of users.
    """
    users: List[UsersGetModel] = Field(..., description="List of users")
    totalPages: int = Field(..., ge=1, description="Total number of pages available")
