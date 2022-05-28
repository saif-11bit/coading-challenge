from application import metadata
from sqlalchemy import (
    Table,
    Column,
    String,
    ForeignKey,
    Float
)
from sqlalchemy.dialects.postgresql import (
    UUID,ENUM
)
from models.category import _category_table_name
from models.school import _school_table_name
from enum import Enum


class RaceEnum(str, Enum):
    Asian = "asian"
    Black = "black"
    Hispanic = "hispanic"
    
_race_enrolled_table_name = "race_enrolled"

RaceEnrolled = Table(
    _race_enrolled_table_name,
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
        "race",
        ENUM("asian",
             "black",
             "hispanic",
             name="race_enum",
             create_type=True
            ),
        nullable=False
    ),
    Column("percent", String, nullable=True),
    Column("count", Float, nullable=True)
)