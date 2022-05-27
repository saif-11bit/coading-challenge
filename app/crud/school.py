from uuid import UUID
from application import database
from models.school import School
from sqlalchemy import select
from schemas.school import (
    SchoolInDB,
    SchoolInResp
)
from typing import List


'''
Find school by its ID
'''
async def find_school_by_id(_id: UUID) -> SchoolInResp:
    query = School.select().where(
        School.columns.id == _id
    )
    school = await database.fetch_one(query)
    return school


''' Find school by DBN'''
async def find_school_by_dbn(_dbn: str) -> SchoolInResp:
    query = School.select().where(
        School.columns.DBN == _dbn
    )
    school = await database.fetch_one(query)
    return school


'''
Get all school in DB
'''
async def get_all_school_in_db(
    offset: int = 0,
    limit: int = 10
) -> List[SchoolInResp]:
    query = School.select()
    query = query.offset(offset).limit(limit)
    school = await database.fetch_all(query)
    return school


'''
Get all schools count in DB
'''
async def get_all_school_count_in_db() -> int:
    query = School.count()
    count = await database.execute(query)
    return count


'''
Create New school
'''
async def create_new_school(obj_in: SchoolInDB) -> SchoolInResp:
    query = School.insert()
    values = obj_in.dict()
    await database.execute(query=query, values=values)
    school = await find_school_by_id(obj_in.id)
    return school
