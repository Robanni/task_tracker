from typing import Any, Optional

from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column


class Base(DeclarativeBase):
    id:Any
    __name__:str

    __allow_unmapped = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class Tasks(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    tracker_count: Mapped[int]
    category_id: Mapped[int]

class Categories(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[Optional[str]]
    name: Mapped[str]