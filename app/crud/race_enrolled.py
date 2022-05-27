from application import database
from models.race_enrolled import RaceEnrolled, RaceEnum
from models.category import Category
from models.school import School
from sqlalchemy import select
from schemas.race_enrolled import (
    RaceEnrolledInDB,
    RaceEnrolledInResp
)
from typing import List
from uuid import UUID


'''
Find Race enrolled by id
'''
async def find_race_enrolled_by_id(_id: UUID) -> RaceEnrolledInResp:
    query = RaceEnrolled.select().where(
        RaceEnrolled.columns.id == _id
    )
    race_enrolled = await database.fetch_one(query)
    return race_enrolled


'''
Race Enrolled in DB
'''
async def find_race_enrolled_in_db(
    _category_id: UUID = None,
    _school_id: UUID = None,
    _race:RaceEnum = None,
) -> List[RaceEnrolledInResp]:
    query = RaceEnrolled.select()
    if _category_id:
        query = query.where(
            Category.columns.id == _category_id
        )
    if _school_id:
        query = query.where(
            School.columns.id == _school_id
        )
    if _race:
        query = query.where(
            RaceEnrolled.columns.race == _race
        )
    
    race_enrolled = await database.fetch_all(query)
    return race_enrolled
