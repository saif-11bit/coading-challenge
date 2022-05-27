from fastapi import APIRouter
from api.endpoints import (
    home,
    category,
    school,
    total_enrolled,
    gender_enrolled,
    grade_enrolled,
    race_enrolled
)


api_router = APIRouter()

api_router.include_router(
    home.router,
    prefix="/home",
    tags=["home"]
)

api_router.include_router(
    category.router,
    prefix="/category",
    tags=["category"]
)

api_router.include_router(
    school.router,
    prefix="/school",
    tags=["school"]
)

api_router.include_router(
    total_enrolled.router,
    prefix="/total_enrolled",
    tags=["total_enrolled"]
)

api_router.include_router(
    gender_enrolled.router,
    prefix="/gender_enrolled",
    tags=["gender_enrolled"]
)

api_router.include_router(
    grade_enrolled.router,
    prefix="/grade_enrolled",
    tags=["grade_enrolled"]
)

api_router.include_router(
    race_enrolled.router,
    prefix="/race_enrolled",
    tags=["race_enrolled"]
)
