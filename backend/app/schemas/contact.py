from pydantic import BaseModel, EmailStr, Field, model_validator
from datetime import datetime

class ContactCreate(BaseModel):
    name: str = Field(..., max_length=100)
    email: EmailStr
    phone: str = Field(..., max_length=20)
    subject: str = Field(..., max_length=200)
    message: str = Field(..., max_length=2000)
    honeypot: str | None = Field(None, max_length=100)

    model_config = {
        'extra': 'forbid'
    }

    @model_validator(mode='after')
    def validate_phone(cls, values):
        phone = values.get('phone')
        if phone is None:
            return values
        if not (phone.startswith('+880') and len(phone) == 14 or phone.startswith('01') and len(phone) == 11):
            raise ValueError('Phone must be in Bangladeshi format +880XXXXXXXXXX or 01XXXXXXXXX')
        return values

    @model_validator(mode='after')
    def validate_honeypot(cls, values):
        if values.get('honeypot'):
            raise ValueError('Bot detected')
        return values


class ContactResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    phone: str
    subject: str
    message: str
    created_at: datetime

    model_config = {
        'from_attributes': True,
        'extra': 'forbid'
    }
