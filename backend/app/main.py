from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.cors import CORSMiddleware
from app.database import lifespan
from app.config import settings
from app.routers import auth, users, contact, admin

app = FastAPI(
    title='KSI Bangladesh API',
    description='Backend API for KSI Bangladesh portal',
    version='1.0.0',
    lifespan=lifespan,
)

app.add_middleware(GZipMiddleware, minimum_size=1000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(contact.router)
app.include_router(admin.router)

@app.get('/')
async def root():
    return {'message': 'KSI Bangladesh backend is running'}
