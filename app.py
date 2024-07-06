from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import secrets

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'  # Update with your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = secrets.token_hex(16)  # Replace with your secret key for JWT encoding

# Initialize extensions
db = SQLAlchemy(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Enable CORS
CORS(app)

# Register blueprints
from api import amenity_controller, city_controller, country_city_controller, country_controller, place_controller, review_controller, user_controller

app.register_blueprint(amenity_controller)
app.register_blueprint(city_controller)
app.register_blueprint(country_city_controller)
app.register_blueprint(country_controller)
app.register_blueprint(place_controller)
app.register_blueprint(review_controller)
app.register_blueprint(user_controller)

# Error handling for JWT
@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({
        'error': 'Token has expired',
        'message': 'Please refresh your token and try again'
    }), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'error': 'Invalid token',
        'message': 'Signature verification failed'
    }), 401

@jwt.unauthorized_loader
def unauthorized_callback(error):
    return jsonify({
        'error': 'Unauthorized',
        'message': 'Missing Authorization header'
    }), 401

@jwt.needs_fresh_token_loader
def token_not_fresh_callback():
    return jsonify({
        'error': 'Fresh token required',
        'message': 'Token is not fresh. Please authenticate again.'
    }), 401

@jwt.revoked_token_loader
def revoked_token_callback():
    return jsonify({
        'error': 'Revoked token',
        'message': 'The token has been revoked'
    }), 401

if __name__ == '__main__':
    manager.run()
