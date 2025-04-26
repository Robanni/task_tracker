from typing import Any

from sqlalchemy.orm import DeclarativeBase, declared_attr



class Base(DeclarativeBase):
    id:Any
    __name__:str

    __allow_unmapped = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()