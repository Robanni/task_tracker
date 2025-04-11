from sqlalchemy.orm.session import Session
from settings import Settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

settings = Settings()

engine = create_engine(settings.get_database_url)

Session = sessionmaker(engine)

def get_db():
    return Session()