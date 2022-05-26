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


class GenderEnum(str, Enum):
    Male = "male"
    Female = "female"


_gender_enrolled_table_name = "gender_enrolled"

GenderEnrolled = Table(
    _gender_enrolled_table_name,
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
        "gender",
        ENUM("male", "female", name="gender_enum", create_type=True),
        nullable=False
    ),
    Column("percent", String, nullable=True),
    Column("count", String, nullable=True)
)