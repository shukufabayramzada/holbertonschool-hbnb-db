# api/user_controller.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models.user import User

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/login', methods=['POST'])
def login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity={'email': user.email, 'is_admin': user.is_admin})
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Bad email or password"}), 401

@user_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@user_bp.route('/admin', methods=['GET'])
@jwt_required()
def admin():
    current_user = get_jwt_identity()
    if current_user['is_admin']:
        return jsonify(msg="Welcome Admin"), 200
    else:
        return jsonify(msg="Admins only!"), 403
