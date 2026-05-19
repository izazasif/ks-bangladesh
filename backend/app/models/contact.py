from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class ContactInDB(BaseModel):
    name: str
    email: EmailStr
    phone: str
    subject: str
    message: str
    created_at: datetime

    model_config = {
        'extra': 'forbid'
    }
