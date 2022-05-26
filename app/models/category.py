from application import metadata
from sqlalchemy import (
    Table,
    Column,
    String
)
from sqlalchemy.dialects.postgresql import (
    UUID
)

_category_table_name = "categories"

Category = Table(
    _category_table_name,
    metadata,
    Column("id", UUID, primary_key=True),
    Column("category_name", String, nullable=True),
)