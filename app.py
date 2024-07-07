from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv
import os
import secrets

# Load environment variables from .env file
load_dotenv()

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    
    # Configure Database
    DATABASE_TYPE = os.getenv('DATABASE_TYPE', 'sqlite')
    if (DATABASE_TYPE == 'sqlite'):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = secrets.token_hex(16)
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'super-secret')

    db.init_app(app)
    migrate = Migrate(app, db)
    CORS(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Import and register Blueprints
    from api.amenity_controller import amenity_controller
    from api.city_controller import city_controller
    from api.country_city_controller import country_city_controller
    from api.country_controller import country_controller
    from api.place_controller import place_controller
    from api.review_controller import review_controller
    from api.user_controller import user_bp

    app.register_blueprint(amenity_controller, url_prefix='/api')
    app.register_blueprint(city_controller, url_prefix='/api')
    app.register_blueprint(country_city_controller, url_prefix='/api')
    app.register_blueprint(country_controller, url_prefix='/api')
    app.register_blueprint(place_controller, url_prefix='/api')
    app.register_blueprint(review_controller, url_prefix='/api')
    app.register_blueprint(user_bp, url_prefix='/api')

    # Default route
    @app.route('/')
    def home():
        return "Welcome to hbhb project part 2"

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
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
    def token_not_fresh_callback(jwt_header, jwt_payload):
        return jsonify({
            'error': 'Fresh token required',
            'message': 'Token is not fresh. Please authenticate again.'
        }), 401

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return jsonify({
            'error': 'Revoked token',
            'message': 'The token has been revoked'
        }), 401

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True if os.getenv('ENV') == 'development' else False)
