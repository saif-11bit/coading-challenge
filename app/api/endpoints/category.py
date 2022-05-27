from fastapi import (
    APIRouter,
    HTTPException,
    status as status_codes
)
from schemas.category import (
    CategoryInResp,
    CategoriesInResp,
    CategoryCreation,
    CategoryInDB
)
from uuid import UUID, uuid4
from crud.category import (
    find_category_by_id,
    get_all_categories_in_db,
    create_new_category
)

router = APIRouter()


@router.post("/", response_model=CategoryInResp)
async def create_category(
    category_in: CategoryCreation
):
    """
    Create a category.
    """
    category = await create_new_category(
        CategoryInDB(
            **category_in.dict(),
            id=uuid4()
        )
    )
    return category


@router.get("/", response_model=CategoriesInResp)
async def get_categories_in_db(
):
    """
    Returns categories list object in DB.
    """
    categories = await get_all_categories_in_db()
    return CategoriesInResp(categories=categories)


@router.get("/{category_id}", response_model=CategoryInResp)
async def get_category_by_id(
    category_id: UUID,
):
    """
    Returns a category object for the specified ID.
    """
    category = await find_category_by_id(
        category_id,
    )
    if not category:
        raise HTTPException(status_codes.HTTP_404_NOT_FOUND, None)
    return category
