from backend.db.base_class import Base
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from backend.models.associations import series_groups

class Series(Base):
    __tablename__ = "series"

    id: Mapped[Integer] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    source: Mapped[str] = mapped_column(String(255))
    url: Mapped[str] = mapped_column(String(255))
    latest_chapter: Mapped[str] = mapped_column(String(255))

    groups = relationship("Group", secondary=series_groups, back_populates="series")

