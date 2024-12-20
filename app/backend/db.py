
"""
SQLAlchemy==2.0.36
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import sqlite3
from sqlalchemy.orm import Session

# \app\models
_DBS_="sqlite:///./taskmanager.db"
# \root
#_DBS_="sqlite:///../../taskmanager.db"

#engine = create_engine(_DBS_, echo=True, pool_size=10, max_overflow=20)
engine = create_engine(_DBS_, pool_pre_ping=True)

SessionLocal= sessionmaker(bind=engine)

session=SessionLocal()

class Base(DeclarativeBase):
	pass

def get_name():
	print(engine.url)
	return _DBS_

#print("sql")
#Base.metadata.create_all(bind=engine)
