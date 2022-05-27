from application import database
from models.race_enrolled import RaceEnrolled, RaceEnum
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
    offset: int = 0,
    limit: int = 10,
    _category_id: UUID = None,
    _school_id: UUID = None,
    _race:RaceEnum = None,
) -> List[RaceEnrolledInResp]:
    query = RaceEnrolled.select()
    if _category_id:
        query = query.where(
            RaceEnrolled.columns.category_id == _category_id
        )
    if _school_id:
        query = query.where(
            RaceEnrolled.columns.school_id == _school_id
        )
    if _race:
        query = query.where(
            RaceEnrolled.columns.race == _race
        )
    query = query.offset(offset).limit(limit)
    race_enrolled = await database.fetch_all(query)
    return race_enrolled


'''
Race Enrolled count in DB
'''
async def find_race_enrolled_in_db_count(
    _category_id: UUID = None,
    _school_id: UUID = None,
    _race:RaceEnum = None,
) -> List[RaceEnrolledInResp]:
    query = RaceEnrolled.count()
    if _category_id:
        query = query.where(
            RaceEnrolled.columns.category_id == _category_id
        )
    if _school_id:
        query = query.where(
            RaceEnrolled.columns.school_id == _school_id
        )
    if _race:
        query = query.where(
            RaceEnrolled.columns.race == _race
        )
    
    count = await database.execute(query)
    return count