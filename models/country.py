from models.baseclass import BaseClass
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app import db

class Country(BaseClass, db.Model):
    __tablename__ = 'countries'

    id = Column(String(36), primary_key=True)
    name = Column(String(100), nullable=False)
    country_code = Column(String(3), unique=True, nullable=False)
    cities = relationship('City', backref='country', lazy=True)

    def __init__(self, name=None, country_code=None, id=None, created_at=None, updated_at=None):
        super().__init__(id=id, created_at=created_at, updated_at=updated_at)
        self.name = name
        self.country_code = country_code

    @staticmethod
    def get_all_countries():
        return Country.query.all()

    @staticmethod
    def get_country_by_code(country_code):
        return Country.query.filter_by(country_code=country_code).first()

    @staticmethod
    def get_cities_by_country_code(country_code):
        country = Country.query.filter_by(country_code=country_code).first()
        return country.cities if country else []

    def country_code_check(self, country_code):
        if country_code.isalnum():
            return True
        raise ValueError("Country code must be alphanumeric")
