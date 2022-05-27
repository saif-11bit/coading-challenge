from application import database
from models.total_enrolled import TotalEnrolled
from models.category import Category
from models.school import School
from sqlalchemy import select
from schemas.total_enrolled import (
    TotalEnrolledInDB,
    TotalEnrolledInResp
)
from typing import List
from uuid import UUID

'''
Find total enrolled by id
'''
async def find_total_enrolled_by_id(_id: UUID) -> TotalEnrolledInResp:
    query = TotalEnrolled.select().where(
        TotalEnrolled.columns.id == _id
    )
    ttl_enrolled = await database.fetch_one(query)
    return ttl_enrolled


'''
find total enrolled in DB
'''
async def total_enrolled_in_db(
    _category_id: UUID = None,
    _school_id: UUID = None
) -> List[TotalEnrolledInResp]:
    query = TotalEnrolled.select()
    
    if _category_id:
        query = query.where(
            Category.columns.id == _category_id
        )
    if _school_id:
        query = query.where(
            School.columns.id == _school_id
        )
    
    total_enrolled = await database.fetch_all(query)
    return total_enrolled

