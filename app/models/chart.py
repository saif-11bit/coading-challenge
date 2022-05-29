from application import metadata
from sqlalchemy import (
    Float,
    Table,
    Column,
    String,
    ForeignKey
)
from sqlalchemy.dialects.postgresql import (
    UUID,
    JSON
)
from models.category import _category_table_name


_chart_enrolled_table_name = "chart_enrolled"

ChartEnrolled = Table(
    _chart_enrolled_table_name,
    metadata,
    Column("id", UUID, primary_key=True),
    Column('enrollment_type', String, nullable=True),
    Column('mean_data', JSON, nullable=True)
)