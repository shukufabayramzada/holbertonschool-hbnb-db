from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from Model.baseclass import BaseClass

Base = declarative_base()

class City(Base):
    __tablename__ = 'cities'
    
    id = Column(Integer(36), primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(50), nullable=False)
    country_id = Column(Integer(36), ForeignKey('countries.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __init__(self, name, country_id, id=None, created_at=None, updated_at=None):
        if id:
            self.id = id
        if created_at:
            self.created_at = created_at
        if updated_at:
            self.updated_at = updated_at
        
        self.name = name
        self.country_id = country_id
    
    @staticmethod
    def get_all_cities(session):
        return session.query(City).all()

    @staticmethod
    def get_city_by_id(session, city_id):
        return session.query(City).filter(City.id == city_id).first()
    
    def country_id_check(self, country_id):
        if isinstance(country_id, int):
            return True
        raise ValueError("Country ID must be numeric")
