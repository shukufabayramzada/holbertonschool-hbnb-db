from models.baseclass import BaseClass
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app import db

class User(BaseClass, db.Model):
    __tablename__ = 'users'

    id = Column(String(36), primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    is_admin = Column(String(128), default=False)
    reviews = relationship('Review', backref='user', lazy=True)
    amenities = relationship('Amenity', backref='user', lazy=True)

    def __init__(self, name, email, password, is_admin=False, id=None, created_at=None, updated_at=None):
        super().__init__(id=id, created_at=created_at, updated_at=updated_at)
        self.name = name
        self.email = email
        self.password = password
        self.is_admin = is_admin
