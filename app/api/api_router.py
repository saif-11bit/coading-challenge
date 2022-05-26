from fastapi import APIRouter
from api.endpoints import home


api_router = APIRouter()

api_router.include_router(
    home.router,
    prefix="/home",
    tags=["home"]
)