from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from models.place import Place
from persistence.data_manager import DataManager

place_controller = Blueprint('place_controller', __name__)
data_manager = DataManager()

@place_controller.route('/places', methods=['POST'])
@jwt_required()
def post_place():
    data = request.get_json()
    place = Place(
        name=data.get('name'),
        description=data.get('description'),
        address=data.get('address'),
        latitude=data.get('latitude'),
        longitude=data.get('longitude'),
        host=data.get('host'),
        number_of_rooms=data.get('number_of_rooms'),
        bath_rooms=data.get('bath_rooms'),
        price_per_night=data.get('price_per_night'),
        max_guests=data.get('max_guests'),
        amenities=data.get('amenities'),
        reviews=data.get('reviews'),
        created_at=data.get('created_at'),
        updated_at=data.get('updated_at')
    )
    data_manager.save(place)
    return jsonify(place.to_dict()), 201

@place_controller.route('/places/<place_id>', methods=['GET'])
@jwt_required()
def get_place(place_id):
    place = data_manager.get(entity_id=place_id, entity_type='Place')
    if place is None:
        return jsonify({"error": "Place not found"}), 404
    return jsonify(place.to_dict()), 200

@place_controller.route('/places/<place_id>', methods=['PUT'])
@jwt_required()
def update_place(place_id):
    data = request.get_json()
    place = data_manager.get(entity_id=place_id, entity_type='Place')
    if place is None:
        return jsonify({"error": "Place not found"}), 404

    place.name = data.get('name', place.name)
    place.description = data.get('description', place.description)
    place.address = data.get('address', place.address)
    place.latitude = data.get('latitude', place.latitude)
    place.longitude = data.get('longitude', place.longitude)
    place.host = data.get('host', place.host)
    place.number_of_rooms = data.get('number_of_rooms', place.number_of_rooms)
    place.bath_rooms = data.get('bath_rooms', place.bath_rooms)
    place.price_per_night = data.get('price_per_night', place.price_per_night)
    place.max_guests = data.get('max_guests', place.max_guests)
    place.amenities = data.get('amenities', place.amenities)
    place.reviews = data.get('reviews', place.reviews)
    place.updated_at = data.get('updated_at', place.updated_at)

    data_manager.update(place)
    return jsonify(place.to_dict()), 200

@place_controller.route('/places/<place_id>', methods=['DELETE'])
@jwt_required()
def delete_place(place_id):
    place = data_manager.get(entity_id=place_id, entity_type='Place')
    if place is None:
        return jsonify({"error": "Place not found"}), 404
    data_manager.delete(entity_id=place_id, entity_type='Place')
    return jsonify({'message': 'Place deleted'}), 204
