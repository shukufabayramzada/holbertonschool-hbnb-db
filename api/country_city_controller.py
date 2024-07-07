from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from persistence.data_manager import DataManager
from models.city import City
from models.country import Country

country_city_controller = Blueprint('country_city_controller', __name__)
data_manager = DataManager()

@country_city_controller.route('/countries', methods=['GET'])
@jwt_required()
def get_countries():
    countries = Country.query.all()
    return jsonify([country.to_dict() for country in countries]), 200

@country_city_controller.route('/countries/<country_code>', methods=['GET'])
@jwt_required()
def get_country(country_code):
    country = Country.query.filter_by(code=country_code).first()
    if country is None:
        return jsonify({'error': 'Country not found'}), 404
    return jsonify(country.to_dict()), 200

@country_city_controller.route('/countries/<country_code>/cities', methods=['GET'])
@jwt_required()
def get_cities_by_country(country_code):
    cities = City.query.filter_by(country_code=country_code).all()
    if not cities:
        return jsonify({'error': 'No cities found for this country'}), 404
    return jsonify([city.to_dict() for city in cities]), 200

@country_city_controller.route('/cities', methods=['POST'])
@jwt_required()
def post_city():
    data = request.get_json()
    city = City(
        name=data['name'],
        country_code=data['country_code'],
        created_at=data['created_at'],
        updated_at=data['updated_at']
    )
    data_manager.save(city)
    return jsonify(city.to_dict()), 201

@country_city_controller.route('/cities', methods=['GET'])
@jwt_required()
def get_cities():
    cities = City.query.all()
    return jsonify([city.to_dict() for city in cities]), 200

@country_city_controller.route('/cities/<city_id>', methods=['GET'])
@jwt_required()
def get_city(city_id):
    city = City.query.get(city_id)
    if city is None:
        return jsonify({'error': 'City not found'}), 404
    return jsonify(city.to_dict()), 200

@country_city_controller.route('/cities/<city_id>', methods=['PUT'])
@jwt_required()
def update_city(city_id):
    data = request.get_json()
    city = data_manager.get(entity_id=city_id, entity_type='City')
    if city is None:
        return jsonify({"error": "City not found"}), 404

    city.name = data.get('name', city.name)
    city.country_code = data.get('country_code', city.country_code)
    city.updated_at = data.get('updated_at', city.updated_at)

    data_manager.update(city)
    return jsonify(city.to_dict()), 200

@country_city_controller.route('/cities/<city_id>', methods=['DELETE'])
@jwt_required()
def delete_city(city_id):
    city = data_manager.get(entity_id=city_id, entity_type='City')
    if city is None:
        return jsonify({'error': 'City not found'}), 404
    data_manager.delete(entity_id=city_id, entity_type='City')
    return jsonify({'message': 'City deleted'}), 204
