from fastapi import APIRouter
# from app.core.config import settings

router = APIRouter()

@router.get('/')
def get_users():
    return 'users'