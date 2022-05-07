from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


password = input("Enter password: ")
engine = create_engine(f"postgresql://postgres:{password}@localhost:5432/cloudnote-db")

Session = sessionmaker(bind= engine)
session = Session()

from .models import User, Note