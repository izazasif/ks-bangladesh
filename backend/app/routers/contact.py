from fastapi import APIRouter, HTTPException, status, Depends
from app.database import get_db
from app.schemas.contact import ContactCreate, ContactResponse
from app.utils.jwt import require_admin, get_current_user
from datetime import datetime

router = APIRouter(prefix='/api/contact', tags=['contact'])

@router.post('', response_model=ContactResponse, status_code=status.HTTP_201_CREATED)
async def submit_contact(payload: ContactCreate):
    db = get_db()
    contact_data = payload.model_dump()
    contact_data['created_at'] = datetime.utcnow()
    result = await db.contacts.insert_one(contact_data)
    contact_data['id'] = str(result.inserted_id)
    return contact_data

@router.get('', response_model=list[ContactResponse])
async def list_contacts(current_user: dict = Depends(require_admin), skip: int = 0, limit: int = 10):
    db = get_db()
    cursor = db.contacts.find().skip(skip).limit(limit).sort('created_at', -1)
    contacts = []
    async for item in cursor:
        item['id'] = str(item['_id'])
        contacts.append(item)
    return contacts

@router.get('/me', response_model=list[ContactResponse])
async def my_contacts(current_user: dict = Depends(get_current_user), skip: int = 0, limit: int = 10):
    db = get_db()
    cursor = db.contacts.find({'email': current_user['email']}).skip(skip).limit(limit).sort('created_at', -1)
    contacts = []
    async for item in cursor:
        item['id'] = str(item['_id'])
        contacts.append(item)
    return contacts
