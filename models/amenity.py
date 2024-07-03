from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Amenities(Base):
    __tablename__ = 'amenities'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    # Example of relationship - adjust as per your needs
    places = relationship("Place", back_populates="amenities")

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"Amenity {self.id}: {self.name}"

    # Example of methods to add and remove places
    def add_place(self, place):
        self.places.append(place)
    
    def remove_place(self, place):
        self.places.remove(place)
