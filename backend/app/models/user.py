from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Literal

class UserInDB(BaseModel):
    name: str
    email: EmailStr
    mobile: str
    purpose: str
    service_interest: str
    user_type: Literal['Individual', 'Business', 'Government', 'NGO']
    hashed_password: str
    role: str
    created_at: datetime

    model_config = {
        'extra': 'forbid'
    }
