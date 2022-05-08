from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    notes = relationship("Note", backref="author")

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self) -> str:
        return f"<User (username= {self.username})>"

class Note(Base):
    __tablename__ = "note"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    text = Column(Text, nullable=False)
    date = Column(DateTime, default=datetime.now(), nullable= False)
    author_id = Column(Integer, ForeignKey("user.id"))

    def __repr__(self) -> str:
        return f"<Note(title={self.name}, date={str(self.date)}, author={self.author_id})>"
