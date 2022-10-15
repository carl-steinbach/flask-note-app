"""The sqlite database models"""
from sqlalchemy import Column, ForeignKey, Integer, String, Text, delete
from sqlalchemy.orm import relationship
from . import db

# declarative configuration of tables
class User(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    notes = relationship("Note", backref='user', cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return '<{}, {}>'.format(self.id, self.email)

class Note(db.Model):
    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey("user.id"))
    title = Column(Text)
    content = Column(Text)

    def __repr__(self) -> str:
        return '<{}, {}>'.format(self.title, self.author)

