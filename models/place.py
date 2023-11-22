#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel Base
from models.review import Review
from sqlalchemy import Float
from sqlachelmy import String
from sqlalchemy import Integer
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Table
from sqlalchemy import Amenity
from sqlalchemy.orm import relationship

association_table = Table("place_amenity", Base.metadata, Column("place_id",
    string(60), ForeignKey("places.id"), primary_key=True, nullable=False),
    Column("amenity_id", string(60), ForeignKey("amenities.id"),
        primary_key=True, nullable=False))


class Place(BaseModel):
    """ A place to stay """

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(string(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity = relationship("Amenity", secondary="place_amenity", viewonly=False)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        def amenity(self): @property
            amenity_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
                return amenity_list

            def reviews(self): @property
                reviews_list = []
                for reviews in list(models.storage.all(Reviews).values()):
                    if reviews.id in self.review_ids:
                        reviews_list.append(reviews)
                        return reviews_list
