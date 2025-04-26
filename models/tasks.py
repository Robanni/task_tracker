from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Tasks(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    tracker_count: Mapped[int]
    category_id: Mapped[int]


class Categories(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[Optional[str]]
    name: Mapped[str]
