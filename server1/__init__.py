from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from server1.credentials import username, password, host, port, db_name

username = username
password = password
host = host
port = port
db_name = db_name
engine = create_engine(f"postgresql://{username}:{password}@{host}:{port}/{db_name}")

Session = sessionmaker(bind= engine)
session = Session()

from .models import User, Note