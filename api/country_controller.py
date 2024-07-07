from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from models.country import Country
from persistence.data_manager import DataManager

country_controller = Blueprint('country_controller', __name__)
data_manager = DataManager()

@country_controller.route('/countries', methods=['POST'])
@jwt_required()
def post_country():
    data = request.get_json()
    country = Country(
        name=data.get('name'),
        code=data.get('code'),
        created_at=data.get('created_at'),
        updated_at=data.get('updated_at')
    )
    data_manager.save(country)
    return jsonify(country.to_dict()), 201

@country_controller.route('/countries/<country_id>', methods=['GET'])
@jwt_required()
def get_country(country_id):
    country = data_manager.get(entity_id=country_id, entity_type='Country')
    if country is None:
        return jsonify({"error": "Country not found"}), 404
    return jsonify(country.to_dict()), 200
