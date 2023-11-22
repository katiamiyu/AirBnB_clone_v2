#!/usr/bin/python3
""" City Module for HBNB project """
from models import storage_type
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ForeignKey
import sqlalchemy
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """
    creates city object
    """
    if storage_type == 'db':
        __tablename__ = "cities"

        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("places", backref="cities", cascade="delete")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """
        constructor function
        """
        super().__init__(*args, **kwargs)
