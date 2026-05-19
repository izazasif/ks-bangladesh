from fastapi import APIRouter, Depends, HTTPException, Response, status, Cookie
from fastapi.responses import JSONResponse
from app.schemas.user import UserCreate, LoginRequest, TokenResponse
from app.database import get_db
from app.utils.hashing import hash_password, verify_password
from app.utils.jwt import create_access_token, create_refresh_token, validate_refresh_token, get_current_user
from app.config import settings
from datetime import datetime

router = APIRouter(prefix='/api/auth', tags=['auth'])

@router.post('/register', status_code=status.HTTP_201_CREATED)
async def register_user(payload: UserCreate):
    db = get_db()
    existing = await db.users.find_one({'email': payload.email})
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Email is already registered')
    user_data = payload.model_dump()
    user_data['hashed_password'] = hash_password(user_data.pop('password'))
    user_data['role'] = 'user'
    user_data['created_at'] = datetime.utcnow()
    await db.users.insert_one(user_data)
    return {'message': 'Registration successful'}

@router.post('/login', response_model=TokenResponse)
async def login_user(payload: LoginRequest):
    db = get_db()
    user = await db.users.find_one({'email': payload.email})
    if not user or not verify_password(payload.password, user['hashed_password']):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid credentials')
    access_token = create_access_token(subject=user['email'], role=user['role'])
    refresh_token, expires = create_refresh_token(subject=user['email'])
    await db.refresh_tokens.insert_one({
        'token': refresh_token,
        'email': user['email'],
        'expires_at': expires,
    })
    response = JSONResponse({'access_token': access_token, 'token_type': 'bearer'})
    response.set_cookie(
        key='refresh_token',
        value=refresh_token,
        httponly=True,
        secure=False,
        samesite='lax',
        path='/api/auth',
        max_age=settings.REFRESH_TOKEN_EXPIRE_DAYS * 24 * 3600,
    )
    return response

@router.post('/refresh', response_model=TokenResponse)
async def refresh_token(refresh_token: str | None = Cookie(None)):
    payload = await validate_refresh_token(refresh_token)
    email = payload.get('sub')
    db = get_db()
    existing = await db.refresh_tokens.find_one({'token': refresh_token})
    if not existing:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid refresh token')
    user = await db.users.find_one({'email': email})
    await db.token_blacklist.insert_one({'token': refresh_token, 'expires_at': datetime.utcfromtimestamp(payload['exp'])})
    access_token = create_access_token(subject=email, role=user.get('role') if user else 'user')
    new_refresh_token, expires = create_refresh_token(subject=email)
    await db.refresh_tokens.insert_one({'token': new_refresh_token, 'email': email, 'expires_at': expires})
    response = JSONResponse({'access_token': access_token, 'token_type': 'bearer'})
    response.set_cookie(
        key='refresh_token',
        value=new_refresh_token,
        httponly=True,
        secure=False,
        samesite='lax',
        path='/api/auth',
        max_age=settings.REFRESH_TOKEN_EXPIRE_DAYS * 24 * 3600,
    )
    return response

@router.get('/me')
async def me(current_user: dict = Depends(get_current_user)):
    return current_user

@router.post('/logout')
async def logout(refresh_token: str | None = Cookie(None)):
    db = get_db()
    if refresh_token:
        payload = await validate_refresh_token(refresh_token)
        await db.token_blacklist.insert_one({'token': refresh_token, 'expires_at': datetime.utcfromtimestamp(payload['exp'])})
    response = Response(status_code=status.HTTP_204_NO_CONTENT)
    response.delete_cookie('refresh_token', path='/api/auth')
    return response
