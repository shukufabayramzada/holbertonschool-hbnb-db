from models.baseclass import BaseClass
from sqlalchemy import Column, String, Integer, ForeignKey
from app import db

class Review(BaseClass, db.Model):
    __tablename__ = 'reviews'

    id = Column(String(36), primary_key=True)
    place_id = Column(String(36), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(String(500), nullable=True)

    def __init__(self, place_id, user_id, rating, comment, id=None, created_at=None, updated_at=None):
        super().__init__(id=id, created_at=created_at, updated_at=updated_at)
        self.place_id = place_id
        self.user_id = user_id
        self.rating = rating
        self.comment = comment

    def add_rating(self, rating):
        if 1 <= rating <= 5:
            self.rating = rating
        else:
            raise ValueError("Ratings must be from 1 to 5")
