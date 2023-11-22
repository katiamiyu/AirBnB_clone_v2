#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from models import storage_type
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if storage_type == 'db':
        __tablename__ = "users"

        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("place", backref="user", casacade="delete")
        reviews = relationship("reviews", backref="user", cascade="delete")
    else:
        first_name = ''
        last_name = ''
        email = ''
        password = ''
