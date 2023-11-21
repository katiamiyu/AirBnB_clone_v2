#!/usr/bin/python3
""" State Module for HBNB project Alx"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models import storage_type


class State(BaseModel, Base):
    """
    create state object and orm
    """
    if storage_type == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """
        constructor function
        """
        super().__init__(*args, **kwargs)

    @property
    def cities(self):
        """ selects all cities of the current state
        """
        my_cities = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                my_cities.append(city)
        return my_cities
