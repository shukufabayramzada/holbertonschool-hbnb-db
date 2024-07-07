from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from models.review import Review
from persistence.data_manager import DataManager

review_controller = Blueprint('review_controller', __name__)
data_manager = DataManager()

@review_controller.route('/reviews', methods=['POST'])
@jwt_required()
def post_review():
    data = request.get_json()
    review = Review(
        user_id=data.get('user_id'),
        place_id=data.get('place_id'),
        text=data.get('text'),
        rating=data.get('rating'),
        created_at=data.get('created_at'),
        updated_at=data.get('updated_at')
    )
    data_manager.save(review)
    return jsonify(review.to_dict()), 201

@review_controller.route('/reviews/<review_id>', methods=['GET'])
@jwt_required()
def get_review(review_id):
    review = data_manager.get(entity_id=review_id, entity_type='Review')
    if review is None:
        return jsonify({"error": "Review not found"}), 404
    return jsonify(review.to_dict()), 200

@review_controller.route('/reviews/<review_id>', methods=['PUT'])
@jwt_required()
def update_review(review_id):
    data = request.get_json()
    review = data_manager.get(entity_id=review_id, entity_type='Review')
    if review is None:
        return jsonify({"error": "Review not found"}), 404

    review.text = data.get('text', review.text)
    review.rating = data.get('rating', review.rating)
    review.updated_at = data.get('updated_at', review.updated_at)

    data_manager.update(review)
    return jsonify(review.to_dict()), 200

@review_controller.route('/reviews/<review_id>', methods=['DELETE'])
@jwt_required()
def delete_review(review_id):
    review = data_manager.get(entity_id=review_id, entity_type='Review')
    if review is None:
        return jsonify({"error": "Review not found"}), 404
    data_manager.delete(entity_id=review_id, entity_type='Review')
    return jsonify({'message': 'Review deleted'}), 204
