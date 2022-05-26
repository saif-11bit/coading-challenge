from application import metadata
from sqlalchemy import (
    Table,
    Column,
    String,
)
from sqlalchemy.dialects.postgresql import (
    UUID
)

_school_table_name = "schools"

School = Table(
    _school_table_name,
    metadata,
    Column("id", UUID, primary_key=True),
    Column("DBN", String, nullable=True),
    Column("school_name", String, nullable=True)
)