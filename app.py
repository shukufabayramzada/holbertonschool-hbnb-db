# app.py
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_cors import CORS
import secrets
from database import db
from api.user_controller import user_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = secrets.token_hex(16)

    db.init_app(app)
    migrate = Migrate(app, db)
    CORS(app)

    app.register_blueprint(user_bp)

    jwt = JWTManager(app)

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

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
