from fastapi import (
    APIRouter,
    HTTPException,
    status as status_codes
)
from schemas.grade_enrolled import (
    GradeEnrolledInResp,
    GradeEnrollmentsInResp
)
from uuid import UUID, uuid4
from crud.grade_enrolled import (
    find_grade_enrolled_by_id,
    find_grade_enrolled_in_db,
    find_grade_enrolled_in_db_count
    
)
from models.grade_enrolled import GradeEnum
from fastapi.encoders import jsonable_encoder
from utils.worker_tasks import create_chart
router = APIRouter()


@router.get("/", response_model=GradeEnrollmentsInResp)
async def get_grade_enrollments_in_db(
    offset: int = 0,
    limit: int = 10,
    _category_id: UUID = None,
    _school_id: UUID = None,
    _grade:GradeEnum = None,
    _chart:bool = None
):
    """
    Returns grade enrollment objects available in DB.
    If _chart: True, then creates chart of _category_id and _grade
    """
    grade_enrollments = await find_grade_enrolled_in_db(
        offset,
        limit,
        _category_id,
        _school_id,
        _grade
    )
    count = await find_grade_enrolled_in_db_count(
        _category_id,
        _school_id,
        _grade
    )
    if _chart:
        json_data = jsonable_encoder(grade_enrollments)
        chart_uuid = uuid4()
        task = create_chart.delay(chart_uuid,_grade, json_data)
    return GradeEnrollmentsInResp(grade_enrollments=grade_enrollments, total_count=count)


@router.get("/{grade_enr_id}", response_model=GradeEnrolledInResp)
async def get_grade_enrolled_by_id(
    grade_enr_id: UUID,
):
    """
    Returns a grade enrollment object for the specified ID.
    """
    grade_enrolled = await find_grade_enrolled_by_id(
        grade_enr_id
    )
    if not grade_enrolled:
        raise HTTPException(status_codes.HTTP_404_NOT_FOUND, None)
    return grade_enrolled
