from models.baseclass import BaseClass
from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app import db

class Place(BaseClass, db.Model):
    __tablename__ = 'places'

    id = Column(String(36), primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500), nullable=True)
    address = Column(String(200), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    host = Column(String(36), nullable=True)  # Assuming host is a user ID or similar
    number_of_rooms = Column(Integer, nullable=False)
    bath_rooms = Column(Integer, nullable=False)
    price_per_night = Column(Float, nullable=False)
    max_guests = Column(Integer, nullable=False)
    city_id = Column(String(36), ForeignKey('cities.id'), nullable=False)
    amenities = relationship('Amenity', backref='place', lazy=True)
    reviews = relationship('Review', backref='place', lazy=True)

    def __init__(self, name, description, address, latitude, longitude, host, number_of_rooms, bath_rooms, price_per_night, max_guests, id=None, created_at=None, updated_at=None):
        super().__init__(id=id, created_at=created_at, updated_at=updated_at)
        self.name = name
        self.description = description
        self.address = address
        self.latitude = latitude
        self.longitude = longitude
        self.host = host
        self.number_of_rooms = number_of_rooms
        self.bath_rooms = bath_rooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests

    def add_amenity(self, amenity):
        self.amenities.append(amenity)

    def update_amenity(self, past_ame, new_ame):
        if past_ame in self.amenities:
            i = self.amenities.index(past_ame)
            self.amenities[i] = new_ame
        else:
            raise ValueError(f"{past_ame} not found")

    def remove_amenity(self, amenity):
        self.amenities.remove(amenity)

    def new_host(self, new_host):
        if self.host is not None:
            raise ValueError("This place already has a host")
        self.host = new_host

    def delete_host(self):
        self.host = None

    def delete(self):
        self.host = None
        self.amenities = []
        self.reviews = []
        print(f"Place {self.name} has been deleted")
