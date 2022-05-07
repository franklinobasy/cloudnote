from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:Frank6408@localhost:5432/cloudnote-db")

Session = sessionmaker(bind= engine)
session = Session()

from .models import User, Note