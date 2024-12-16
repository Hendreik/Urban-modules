
"""
SQLAlchemy==2.0.36
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column, Integer, String,Boolean, ForeignKey
#from app.models import task,user

engine = create_engine("sqlite:///taskmanager.db", echo=True)

SessionLocal= sessionmaker(bind=engine)

class Base(DeclarativeBase):
	pass


print("sql")
Base.metadata.create_all(bind=engine)
