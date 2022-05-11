from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from server1.credentials import username, password, host, port, db_name

username = username
password = password
host = host
port = port
db_name = db_name
engine = create_engine(f"postgresql://{username}:{password}@{host}:{port}/{db_name}")
#engine = create_engine(f"postgresql://xnmhjmjyyhyiwl:d97d5c5498331ac059f8cbf67197b4fc9f52e29379f883baa4717ec187bd3b9d@ec2-18-210-64-223.compute-1.amazonaws.com:5432/d4oobb9t3dkr3j")
Session = sessionmaker(bind= engine)
session = Session()

from .models import User, Note