from backend.db.base_class import Base
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from backend.models.associations import series_groups


class Group(Base):
    __tablename__ = "groups"

    id: Mapped[Integer] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(255), default="active")
    website: Mapped[str] = mapped_column(String(255))

    series = relationship("Series", secondary=series_groups, back_populates="groups")