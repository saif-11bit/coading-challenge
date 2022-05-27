from uuid import UUID
from application import database
from models.category import Category
from sqlalchemy import select
from schemas.category import (
    CategoryInDB,
    CategoryInResp
)
from typing import List

'''
Find category by its ID
'''
async def find_category_by_id(_id: UUID) -> CategoryInResp:
    query = Category.select().where(
        Category.columns.id == _id
    )
    category = await database.fetch_one(query)
    return category


'''
Get all categories in DB
'''
async def get_all_categories_in_db() -> List[CategoryInResp]:
    query = Category.select()
    categories = await database.fetch_all(query)
    return categories


'''
Create New Category
'''
async def create_new_category(obj_in: CategoryInDB) -> CategoryInResp:
    query = Category.insert()
    values = obj_in.dict()
    await database.execute(query=query, values=values)
    category = await find_category_by_id(obj_in.id)
    return category
