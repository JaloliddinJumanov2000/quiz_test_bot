from sqlalchemy import create_engine, Column, String, Integer, BigInteger
from sqlalchemy.orm import declarative_base, sessionmaker
from data.config import PG_PASS,PG_USER,PG_HOST,PG_PORT,PG_DB

engine = create_engine(f'postgresql+psycopg2://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{PG_DB}', echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True,autoincrement=True)
    chat_id = Column(BigInteger,unique=True)
    fullname = Column(String(50), nullable=False)
    phone = Column(String(20), nullable=False)