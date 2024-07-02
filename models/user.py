from models.baseclass import BaseClass
import re
from app import db



class User(BaseClass):
    __tablename__ = 'users'

    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    host_id = db.Column(db.String(36), nullable=True)
    place_id = db.Column(db.String(36), nullable=True)
    reviews = db.Column(db.JSON, nullable=True, default=[])

    def __init__(self, email, password, first_name, last_name, host_id=None, place_id=None, reviews=None, created_at=None, updated_at=None, id=None):
        super().__init__()
        
        if not self.is_valid_email(email):
            raise ValueError("Invalid email address")
        
        if self.email_check(email):
            raise ValueError("Email address already in use")
        
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.is_admin = False
        self.host_id = host_id
        self.place_id = place_id
        self.reviews = reviews if reviews else []

    @staticmethod
    def email_check(email):
        return User.query.filter_by(email=email).first() is not None

    @staticmethod
    def is_valid_email(email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    def not_own_review(self, host_id, place_id, review):
        if host_id == place_id:
            raise ValueError("Owners can't review their own places")
        self.host_id = host_id
        self.place_id = place_id
        self.reviews.append(review)

    def save(self):
        super().save()
