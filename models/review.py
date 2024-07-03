from sqlalchemy import Column, String, Integer, Float, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from Model.baseclass import BaseClass

class Reviews(BaseClass):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    place = Column(String)
    rating = Column(Integer)
    comment = Column(String)

    def __init__(self, place, rating, comment):
        self.place = place
        self.rating = rating
        self.comment = comment

    def add_rating(self, rating):
        if 1 <= rating <= 5:
            self.rating = rating
        else:
            raise ValueError("Ratings must be from 1 to 5")
