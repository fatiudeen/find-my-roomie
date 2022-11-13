from fastapi import APIRouter
from app.api.v1.routes import users, posts

api_router = APIRouter()
api_router.include_router(users.router, prefix='/users')
api_router.include_router(posts.router, prefix='/posts')
