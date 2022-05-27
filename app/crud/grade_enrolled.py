from application import database
from models.grade_enrolled import GradeEnrolled, GradeEnum
from models.category import Category
from models.school import School
from sqlalchemy import select
from schemas.grade_enrolled import (
    GradeEnrolledInDB,
    GradeEnrolledInResp
)
from typing import List
from uuid import UUID


'''
Find Grade enrolled by id
'''
async def find_grade_enrolled_by_id(_id: UUID) -> GradeEnrolledInResp:
    query = GradeEnrolled.select().where(
        GradeEnrolled.columns.id == _id
    )
    grade_enrolled = await database.fetch_one(query)
    return grade_enrolled


'''
Grade Enrolled in DB
'''
async def find_grade_enrolled_in_db(
    offset: int = 0,
    limit: int = 10,
    _category_id: UUID = None,
    _school_id: UUID = None,
    _grade:GradeEnum = None,
) -> List[GradeEnrolledInResp]:
    query = GradeEnrolled.select()
    if _category_id:
        query = query.where(
            GradeEnrolled.columns.category_id == _category_id
        )
    if _school_id:
        query = query.where(
            GradeEnrolled.columns.school_id == _school_id
        )
    if _grade:
        query = query.where(
            GradeEnrolled.columns.grade == _grade
        )
    query = query.offset(offset).limit(limit)
    grade_enrolled = await database.fetch_all(query)
    return grade_enrolled


'''
Grade Enrolled count in DB
'''
async def find_grade_enrolled_in_db_count(
    _category_id: UUID = None,
    _school_id: UUID = None,
    _grade:GradeEnum = None,
) -> List[GradeEnrolledInResp]:
    query = GradeEnrolled.count()
    if _category_id:
        query = query.where(
            GradeEnrolled.columns.category_id == _category_id
        )
    if _school_id:
        query = query.where(
            GradeEnrolled.columns.school_id == _school_id
        )
    if _grade:
        query = query.where(
            GradeEnrolled.columns.grade == _grade
        )
    
    grade_enrolled = await database.execute(query)
    return grade_enrolled


