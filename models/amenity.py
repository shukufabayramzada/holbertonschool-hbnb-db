from models.baseclass import BaseClass
from sqlalchemy import Column, String
from app import db
from sqlalchemy.orm import relationship

class Amenity(BaseClass, db.Model):
    __tablename__ = 'amenities'

    id = Column(String(36), primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500), nullable=True)
    places = relationship('Place', backref='amenity', lazy=True)

    def __init__(self, name, description, id=None, created_at=None, updated_at=None):
        super().__init__(id=id, created_at=created_at, updated_at=updated_at)
        self.name = name
        self.description = description

    def add_place(self, place):
        self.places.append(place)

    def remove_place(self, place):
        self.places.remove(place)

    def __str__(self):
        return f"Amenity: {self.name}"
