from flask import Flask
from app import db
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.country import Country
from models.place import Place
from models.review import Review

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()
    print("Database tables created.")
