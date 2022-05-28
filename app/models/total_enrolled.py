from application import metadata
from sqlalchemy import (
    Table,
    Column,
    String,
    ForeignKey,
    Float
)
from sqlalchemy.dialects.postgresql import (
    UUID
)
from models.category import _category_table_name
from models.school import _school_table_name

_total_enrolled_table_name = "total_enrolled"

TotalEnrolled = Table(
    _total_enrolled_table_name,
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
    Column("count", Float, nullable=True)
)