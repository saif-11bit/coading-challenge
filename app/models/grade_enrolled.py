from application import metadata
from sqlalchemy import (
    Table,
    Column,
    String,
    ForeignKey
)
from sqlalchemy.dialects.postgresql import (
    UUID,
    ENUM
)
from models.category import _category_table_name
from models.school import _school_table_name
from enum import Enum


class GradeEnum(str, Enum):
    Grade_K = "grade_k"
    Grade_1 = "grade_1"
    Grade_2 = "grade_2"
    Grade_3 = "grade_3"
    Grade_4 = "grade_4" 
    Grade_5 = "grade_5"
    
    
_grade_enrolled_table_name = "grade_enrolled"

GradeEnrolled = Table(
    _grade_enrolled_table_name,
    metadata,
    Column("id", UUID, primary_key=True),
    Column(
        "category_id",
        ForeignKey(
            f"{_category_table_name}.id",ondelete="CASCADE"
        ),
        nullable=True
    ),
    Column(
        "school_id",
        ForeignKey(
            f"{_school_table_name}.id",ondelete="CASCADE"
        ),
        nullable=True
    ),
    Column(
        "grade",
        ENUM("grade_k", "grade_1",
             "grade_2", "grade_3",
             "grade_4", "grade_5",
             name="grade_enum",
             create_type=True
            ),
        nullable=False
    ),
    Column("count", String, nullable=True)
)