from fastapi import APIRouter, Depends, HTTPException, status
from app.database import get_db
from app.schemas.user import UserResponse, UserUpdate
from app.utils.jwt import get_current_user, require_admin
from bson import ObjectId

router = APIRouter(prefix='/api/users', tags=['users'])

@router.get('', response_model=list[UserResponse])
async def list_users(current_user: dict = Depends(require_admin), skip: int = 0, limit: int = 10):
    db = get_db()
    cursor = db.users.find({}, {'hashed_password': 0}).skip(skip).limit(limit).sort('created_at', -1)
    users = []
    async for user in cursor:
        user['id'] = str(user['_id'])
        users.append(user)
    return users

@router.get('/{user_id}', response_model=UserResponse)
async def get_user(user_id: str, current_user: dict = Depends(get_current_user)):
    db = get_db()
    if current_user['role'] != 'admin' and current_user['email'] != user_id and current_user.get('email') != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Insufficient permissions')
    user = await db.users.find_one({'email': user_id} if '@' in user_id else {'_id': ObjectId(user_id)}, {'hashed_password': 0})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    user['id'] = str(user['_id'])
    return user

@router.put('/{user_id}', response_model=UserResponse)
async def update_user(user_id: str, payload: UserUpdate, current_user: dict = Depends(get_current_user)):
    db = get_db()
    target_id = {'email': user_id} if '@' in user_id else {'_id': ObjectId(user_id)}
    if current_user['role'] != 'admin' and current_user['email'] != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Insufficient permissions')
    update_data = payload.model_dump(exclude_none=True)
    if not update_data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='No data provided')
    result = await db.users.update_one(target_id, {'$set': update_data})
    if result.modified_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    user = await db.users.find_one(target_id, {'hashed_password': 0})
    user['id'] = str(user['_id'])
    return user
