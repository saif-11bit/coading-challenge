from fastapi import (
    APIRouter,
    HTTPException,
    status as status_codes
)
from schemas.race_enrolled import (
    RaceEnrolledInResp,
    RaceEnrollmentsInResp
)
from uuid import UUID, uuid4
from crud.race_enrolled import (
    find_race_enrolled_by_id,
    find_race_enrolled_in_db,
    find_race_enrolled_in_db_count
    
)
from models.race_enrolled import RaceEnum

router = APIRouter()


@router.get("/", response_model=RaceEnrollmentsInResp)
async def get_race_enrollments_in_db(
    offset: int = 0,
    limit: int = 10,
    _category_id: UUID = None,
    _school_id: UUID = None,
    _race:RaceEnum = None,
):
    """
    Returns race enrollment objects available in DB.
    """
    race_enrollments = await find_race_enrolled_in_db(
        offset,
        limit,
        _category_id,
        _school_id,
        _race
    )
    count = await find_race_enrolled_in_db_count(
        _category_id,
        _school_id,
        _race
    )
    return RaceEnrollmentsInResp(race_enrollments=race_enrollments, total_count=count)


@router.get("/{race_enr_id}", response_model=RaceEnrolledInResp)
async def get_race_enrolled_by_id(
    race_enr_id: UUID,
):
    """
    Returns a race enrollment object for the specified ID.
    """
    race_enrolled = await find_race_enrolled_by_id(
        race_enr_id
    )
    if not race_enrolled:
        raise HTTPException(status_codes.HTTP_404_NOT_FOUND, None)
    return race_enrolled
