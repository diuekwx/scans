from sqlalchemy import Table, Column, Integer, ForeignKey
from backend.db.base_class import Base

series_groups = Table(
    "series_groups",
    Base.metadata,
    Column("series_id", Integer, ForeignKey("series.id"), primary_key=True),
    Column("group_id", Integer, ForeignKey("groups.id"), primary_key=True),
)
