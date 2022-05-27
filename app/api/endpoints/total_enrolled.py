from fastapi import (
    APIRouter,
    HTTPException,
    status as status_codes
)
from schemas.total_enrolled import (
    TotalEnrolledInDB,
    TotalEnrolledInResp,
    TotalEnrollmentsInResp
)
from uuid import UUID, uuid4
from crud.total_enrolled import (
    find_total_enrolled_by_id,
    total_enrolled_in_db,
    total_enrolled_in_db_count
)

router = APIRouter()


@router.get("/", response_model=TotalEnrollmentsInResp)
async def get_total_enrollments_in_db(
    offset: int = 0,
    limit: int = 10,
    _category_id: UUID = None,
    _school_id: UUID = None
):
    """
    Returns total enrollment objects available in DB.
    """
    total_enrollments = await total_enrolled_in_db(
        offset,
        limit,
        _category_id,
        _school_id
    )
    count = await total_enrolled_in_db_count(
        _category_id,
        _school_id
    )
    return TotalEnrollmentsInResp(total_enrollments=total_enrollments, total_count=count)


@router.get("/{ttl_enr_id}", response_model=TotalEnrolledInResp)
async def get_total_enrollment_by_id(
    ttl_enr_id: UUID,
):
    """
    Returns a total enrollment object for the specified ID.
    """
    total_enrolled = await find_total_enrolled_by_id(
        ttl_enr_id
    )
    if not total_enrolled:
        raise HTTPException(status_codes.HTTP_404_NOT_FOUND, None)
    return total_enrolled
