"""The sqlite database models"""
from sqlalchemy import Column, Integer, String
from . import db

# declarative configuration of tables
class User(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
