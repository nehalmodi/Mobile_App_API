from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

engine = create_engine(
    'postgresql://postgres:7809@localhost/mobile_app',
    echo=True
)

Base = declarative_base()
Session = sessionmaker()