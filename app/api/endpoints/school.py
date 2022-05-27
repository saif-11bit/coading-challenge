from fastapi import (
    APIRouter,
    HTTPException,
    status as status_codes
)
from schemas.school import (
    SchoolInResp,
    SchoolsInResp,
    SchoolCreation,
    SchoolInDB
)
from uuid import UUID, uuid4
from crud.school import (
    find_school_by_id,
    find_school_by_dbn,
    get_all_school_in_db,
    get_all_school_count_in_db,
    create_new_school
)

router = APIRouter()


@router.post("/", response_model=SchoolInResp)
async def create_school(
    school_in: SchoolCreation
):
    """
    Create a school.
    """
    school = await create_new_school(
        SchoolInDB(
            **school_in.dict(),
            id=uuid4()
        )
    )
    return school


@router.get("/", response_model=SchoolsInResp)
async def get_schools_in_db(
    offset: int = 0,
    limit: int = 10
):
    """
    Returns schools list object available in DB.
    """
    schools = await get_all_school_in_db(
        offset,
        limit
    )
    count = await get_all_school_count_in_db()
    return SchoolsInResp(schools=schools, total_count=count)


@router.get("/{school_id}", response_model=SchoolInResp)
async def get_school_by_id(
    school_id: UUID,
):
    """
    Returns a school object for the specified ID.
    """
    school = await find_school_by_id(
        school_id,
    )
    if not school:
        raise HTTPException(status_codes.HTTP_404_NOT_FOUND, None)
    return school


@router.get("/dbn/{school_dbn}", response_model=SchoolInResp)
async def get_school_by_dbn(
    school_dbn: str,
):
    """
    Returns a school object for the specified DBN.
    """
    school = await find_school_by_dbn(
        school_dbn
    )
    if not school:
        raise HTTPException(status_codes.HTTP_404_NOT_FOUND, None)
    return school
