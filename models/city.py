from models.baseclass import BaseClass
from sqlalchemy import Column, String, Integer, ForeignKey
from app import db
from sqlalchemy.orm import relationship

class City(BaseClass, db.Model):
    __tablename__ = 'cities'

    id = Column(String(36), primary_key=True)
    name = Column(String(100), nullable=False)
    country_id = Column(String(36), ForeignKey('countries.id'), nullable=False)
    places = relationship('Place', backref='city', lazy=True)

    def __init__(self, name, country_id, id=None, created_at=None, updated_at=None):
        super().__init__(id=id, created_at=created_at, updated_at=updated_at)
        self.name = name
        self.country_id = country_id

    @staticmethod
    def get_all_cities():
        return City.query.all()

    @staticmethod
    def get_city_by_id(city_id):
        return City.query.filter_by(id=city_id).first()

    def country_id_check(self, country_id):
        if str(country_id).isdigit():
            return True
        raise ValueError("Country ID must be numeric")
