# əmin deyilem

from sqlalchemy import Column, String, Integer, Float, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from Model.baseclass import BaseClass

class Place(BaseClass):
    __tablename__ = 'places'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    address = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    host = Column(String, nullable=False)
    number_of_rooms = Column(Integer, nullable=False)
    bath_rooms = Column(Integer, nullable=False)
    price_per_night = Column(Float, nullable=False)
    max_guests = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    

    amenities = relationship("Amenity", back_populates="place", cascade="all, delete-orphan")
    reviews = relationship("Review", back_populates="place", cascade="all, delete-orphan")

    def __init__(self, name, description, address, latitude, longitude, host, number_of_rooms, bath_rooms, price_per_night, max_guests, id=None, created_at=None, updated_at=None):
        if id:
            self.id = id
        else:
            super().__init__()
        
        if created_at:
            self.created_at = created_at
        if updated_at:
            self.updated_at = updated_at
        
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
        self.amenities = []
        self.reviews = []

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
            raise ValueError("This place already has host")
        self.host = new_host
    
    def delete_host(self):
        self.host = None
        
    def delete(self):
        self.host = None
        self.amenities = []
        self.reviews = []
        print(f"Place {self.name} has been deleted")
