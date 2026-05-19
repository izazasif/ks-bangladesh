from fastapi import APIRouter, Depends
from app.database import get_db
from app.utils.jwt import require_admin

router = APIRouter(prefix='/api/admin', tags=['admin'])

@router.get('/stats')
async def get_stats(current_user: dict = Depends(require_admin)):
    db = get_db()
    total_users = await db.users.count_documents({})
    total_contacts = await db.contacts.count_documents({})
    pipeline = [
        {'$group': {'_id': '$user_type', 'count': {'$sum': 1}}}
    ]
    breakdown = await db.users.aggregate(pipeline).to_list(length=10)
    return {
        'total_users': total_users,
        'total_contacts': total_contacts,
        'users_by_type': {item['_id']: item['count'] for item in breakdown if item['_id']},
    }
