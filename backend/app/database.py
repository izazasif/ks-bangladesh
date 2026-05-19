from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings
from typing import AsyncIterator
from contextlib import asynccontextmanager

client: AsyncIOMotorClient | None = None

def get_db():
    if client is None:
        raise RuntimeError('Database client is not initialized')
    return client[settings.DB_NAME]

@asynccontextmanager
async def lifespan(app):
    global client
    client = AsyncIOMotorClient(settings.MONGODB_URL)
    app.state.db = client[settings.DB_NAME]
    await _create_indexes(app.state.db)
    await _seed_admin(app.state.db)
    try:
        yield
    finally:
        client.close()

async def _create_indexes(db):
    await db.users.create_index('email', unique=True)
    await db.users.create_index('user_type')
    await db.users.create_index('created_at')
    await db.contacts.create_index('created_at')
    await db.contacts.create_index('email')
    await db.refresh_tokens.create_index('token', unique=True)
    await db.refresh_tokens.create_index('expires_at', expireAfterSeconds=0)
    await db.token_blacklist.create_index('token', unique=True)
    await db.token_blacklist.create_index('expires_at', expireAfterSeconds=0)

async def _seed_admin(db):
    existing = await db.users.find_one({'email': settings.ADMIN_EMAIL})
    if existing:
        return
    from app.utils.hashing import hash_password
    admin = {
        'name': 'KSI Admin',
        'email': settings.ADMIN_EMAIL,
        'mobile': '+8801000000000',
        'hashed_password': hash_password(settings.ADMIN_PASSWORD),
        'purpose': 'admin',
        'service_interest': 'General Consultation',
        'user_type': 'Business',
        'role': 'admin',
        'created_at': __import__('datetime').datetime.utcnow(),
    }
    await db.users.insert_one(admin)
