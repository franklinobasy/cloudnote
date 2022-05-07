from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql://postgres:Frank6408@localhost:5432/cloudnote-db")

Session = sessionmaker(bind= engine)
session = Session()

Base = declarative_base()
print("success")