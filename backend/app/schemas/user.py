from pydantic import BaseModel, EmailStr, Field, model_validator
from datetime import datetime
from typing import Literal

class UserBase(BaseModel):
    name: str = Field(..., max_length=100)
    email: EmailStr
    mobile: str = Field(..., max_length=20)
    purpose: str = Field(..., max_length=250)
    service_interest: str = Field(..., max_length=50)
    user_type: Literal['Individual', 'Business', 'Government', 'NGO']

    model_config = {
        'extra': 'forbid'
    }

    @model_validator(mode='after')
    def validate_mobile(cls, values):
        mobile = values.get('mobile')
        if mobile is None:
            return values
        if not (mobile.startswith('+880') and len(mobile) == 14 or mobile.startswith('01') and len(mobile) == 11):
            raise ValueError('Mobile must be in Bangladeshi format +880XXXXXXXXXX or 01XXXXXXXXX')
        return values


class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=128)

    @model_validator(mode='after')
    def validate_password(cls, values):
        password = values.get('password')
        if password:
            if not any(char.isupper() for char in password) or not any(char.isdigit() for char in password):
                raise ValueError('Password must contain at least one uppercase letter and one number')
        return values


class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128)

    model_config = {
        'extra': 'forbid'
    }


class UserResponse(UserBase):
    id: str
    role: str
    created_at: datetime

    model_config = {
        'from_attributes': True,
        'extra': 'forbid'
    }


class UserUpdate(BaseModel):
    name: str | None = Field(None, max_length=100)
    mobile: str | None = Field(None, max_length=20)
    purpose: str | None = Field(None, max_length=250)
    service_interest: str | None = Field(None, max_length=50)
    user_type: Literal['Individual', 'Business', 'Government', 'NGO'] | None = None

    model_config = {
        'extra': 'forbid'
    }

    @model_validator(mode='after')
    def validate_mobile(cls, values):
        mobile = values.get('mobile')
        if mobile is None:
            return values
        if not (mobile.startswith('+880') and len(mobile) == 14 or mobile.startswith('01') and len(mobile) == 11):
            raise ValueError('Mobile must be in Bangladeshi format +880XXXXXXXXXX or 01XXXXXXXXX')
        return values


class TokenPayload(BaseModel):
    sub: str
    role: str | None = None
    exp: int

    model_config = {
        'extra': 'forbid'
    }


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = 'bearer'

    model_config = {
        'extra': 'forbid'
    }
