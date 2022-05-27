from application import database
from models.gender_enrolled import GenderEnrolled, GenderEnum
from models.category import Category
from models.school import School
from sqlalchemy import select
from schemas.gender_enrolled import (
    GenderEnrolledInDB,
    GenderEnrolledInResp
)
from typing import List
from uuid import UUID


'''
Find Gender enrolled by id
'''
async def find_gender_enrolled_by_id(_id: UUID) -> GenderEnrolledInResp:
    query = GenderEnrolled.select().where(
        GenderEnrolled.columns.id == _id
    )
    gender_enrolled = await database.fetch_one(query)
    return gender_enrolled


'''
Gender Enrolled in DB
'''
async def find_gender_enrolled_in_db(
    _category_id: UUID = None,
    _school_id: UUID = None,
    _gender:GenderEnum = None,
) -> List[GenderEnrolledInResp]:
    query = GenderEnrolled.select()
    if _category_id:
        query = query.where(
            Category.columns.id == _category_id
        )
    if _school_id:
        query = query.where(
            School.columns.id == _school_id
        )
    if _gender:
        query = query.where(
            GenderEnrolled.columns.gender == _gender
        )
    
    gender_enrolled = await database.fetch_all(query)
    return gender_enrolled

