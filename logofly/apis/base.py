from fastapi import APIRouter
from apis.v1 import route_user, route_logo, route_login

api_router = APIRouter()

api_router.include_router(router=route_user.router, prefix="/users", tags=["users"])
api_router.include_router(router=route_logo.router, prefix="/logos", tags=["logos"])
api_router.include_router(router=route_login.router, prefix="", tags=["login"])