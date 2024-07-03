from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import City

Base = declarative_base()

class Country(Base):
    __tablename__ = 'countries'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    country_code = Column(String, unique=True)
    cities = relationship("City", back_populates="country")

    def __init__(self, id=None, name=None, country_code=None):
        if id:
            self.id = id
        self.name = name
        self.country_code = country_code

    @staticmethod
    def get_all_countries(session):
        return session.query(Country).all()
    
    @staticmethod
    def get_country_by_code(session, country_code):
        return session.query(Country).filter_by(country_code=country_code).first()
    
    @staticmethod
    def get_cities_by_country_code(session, country_code):
        return session.query(City).filter_by(country_code=country_code).all()
    
    def country_code_check(self, country_code):
        if country_code.isalnum():
            return True
        raise ValueError("Country code must be alphanumeric")
