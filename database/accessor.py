from sqlalchemy.orm.session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import Settings


settings = Settings()

engine = create_engine(settings.get_database_url)

session = sessionmaker(engine)


def get_db() -> Session:
    return session()
