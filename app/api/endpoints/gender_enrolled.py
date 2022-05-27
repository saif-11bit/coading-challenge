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

router = APIRouter()


@router.get("/", response_model=GenderEnrollmentsInResp)
async def get_gender_enrollments_in_db(
    offset: int = 0,
    limit: int = 10,
    _category_id: UUID = None,
    _school_id: UUID = None,
    _gender:GenderEnum = None,
):
    """
    Returns gender enrollment objects available in DB.
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
    return GenderEnrollmentsInResp(gender_enrollments=gender_enrollments, total_count=count)


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
