from fastapi import (
    APIRouter,
    HTTPException,
    status as status_codes
)
from schemas.gender_enrolled import (
    GenderEnrolledInDB,
    GenderEnrolledInResp,
    GenderEnrollmentsInResp
)
from uuid import UUID, uuid4
from crud.gender_enrolled import (
    find_gender_enrolled_by_id,
    find_gender_enrolled_in_db,
    find_gender_enrolled_in_db_count
)
from models.gender_enrolled import GenderEnum
import pandas as pd
from fastapi.encoders import jsonable_encoder
from utils.worker_tasks import create_chart

router = APIRouter()


@router.get("/", response_model=GenderEnrollmentsInResp)
async def get_gender_enrollments_in_db(
    offset: int = 0,
    limit: int = 10,
    _category_id: UUID = None,
    _school_id: UUID = None,
    _gender:GenderEnum = None,
    _chart: bool = None
):
    """
    Returns gender enrollment objects available in DB.
    If _chart: True, then creates chart of _category_id and _gender
    """
    gender_enrollments = await find_gender_enrolled_in_db(
        offset,
        limit,
        _category_id,
        _school_id,
        _gender
    )
    count = await find_gender_enrolled_in_db_count(
        _category_id,
        _school_id,
        _gender
    )

    if _chart:
        json_data = jsonable_encoder(gender_enrollments)
        chart_uuid = uuid4()
        task = create_chart.delay(chart_uuid,_gender, json_data)
    return GenderEnrollmentsInResp(chart_id=chart_uuid, gender_enrollments=gender_enrollments, total_count=count)


@router.get("/{gen_enr_id}", response_model=GenderEnrolledInResp)
async def get_gender_enrolled_by_id(
    gen_enr_id: UUID,
):
    """
    Returns a gender enrollment object for the specified ID.
    """
    gender_enrolled = await find_gender_enrolled_by_id(
        gen_enr_id
    )
    if not gender_enrolled:
        raise HTTPException(status_codes.HTTP_404_NOT_FOUND, None)
    return gender_enrolled
