from fastapi import APIRouter
from api.endpoints import (
    transfer_csv_to_db,
    category,
    school,
    total_enrolled,
    gender_enrolled,
    grade_enrolled,
    race_enrolled,
    chart
)


api_router = APIRouter()

api_router.include_router(
    transfer_csv_to_db.router,
    prefix="/transfer_csv_data",
    tags=["transfer_csv_to_db"]
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

api_router.include_router(
    chart.router,
    prefix="/chart",
    tags=["chart"]
)

