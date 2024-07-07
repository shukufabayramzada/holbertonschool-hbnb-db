from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from models.amenity import Amenity
from persistence.data_manager import DataManager

amenity_controller = Blueprint('amenity_controller', __name__)
data_manager = DataManager()

@amenity_controller.route('/amenities', methods=['POST'])
@jwt_required()
def post_amenity():
    data = request.get_json()
    name = data.get('name')

    if not name:
        return jsonify({"error": "Name is required"}), 400

    amenity = Amenity(
        name=name,
        description=data.get('description'),
        created_at=data.get('created_at'),
        updated_at=data.get('updated_at')
    )
    data_manager.save(amenity)
    return jsonify(amenity.to_dict()), 201

@amenity_controller.route('/amenities', methods=['GET'])
@jwt_required()
def get_amenities():
    amenities = data_manager.get_all('Amenity')
    return jsonify([amenity.to_dict() for amenity in amenities]), 200

@amenity_controller.route('/amenities/<amenity_id>', methods=['GET'])
@jwt_required()
def get_amenity(amenity_id):
    amenity = data_manager.get(entity_id=amenity_id, entity_type='Amenity')
    if amenity is None:
        return jsonify({"error": "Amenity not found"}), 404
    return jsonify(amenity.to_dict()), 200

@amenity_controller.route('/amenities/<amenity_id>', methods=['PUT'])
@jwt_required()
def update_amenity(amenity_id):
    data = request.get_json()
    amenity = data_manager.get(entity_id=amenity_id, entity_type='Amenity')
    if amenity is None:
        return jsonify({"error": "Amenity not found"}), 404

    amenity.name = data.get('name', amenity.name)
    amenity.description = data.get('description', amenity.description)
    amenity.updated_at = data.get('updated_at', amenity.updated_at)

    data_manager.update(amenity)
    return jsonify(amenity.to_dict()), 200

@amenity_controller.route('/amenities/<amenity_id>', methods=['DELETE'])
@jwt_required()
def delete_amenity(amenity_id):
    amenity = data_manager.get(entity_id=amenity_id, entity_type='Amenity')
    if amenity is None:
        return jsonify({"error": "Amenity not found"}), 404
    data_manager.delete(entity_id=amenity_id, entity_type='Amenity')
    return jsonify({'message': 'Amenity deleted'}), 204
