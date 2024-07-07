from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from models.city import City
from persistence.data_manager import DataManager

city_controller = Blueprint('city_controller', __name__)
data_manager = DataManager()

@city_controller.route('/cities', methods=['POST'])
@jwt_required()
def post_city():
    data = request.get_json()
    city = City(
        name=data.get('name'),
        country_id=data.get('country_id'),
        created_at=data.get('created_at'),
        updated_at=data.get('updated_at')
    )
    data_manager.save(city)
    return jsonify(city.to_dict()), 201

@city_controller.route('/cities/<city_id>', methods=['GET'])
@jwt_required()
def get_city(city_id):
    city = data_manager.get(entity_id=city_id, entity_type='City')
    if city is None:
        return jsonify({"error": "City not found"}), 404
    return jsonify(city.to_dict()), 200
