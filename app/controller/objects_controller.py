from flask import Blueprint, jsonify, request
from app.services.objects_service import ObjectsService

objects_bp = Blueprint('objects', __name__)

@objects_bp.route('/objects', methods=['GET'])
def get_all_objects():
    objects = ObjectsService.get_all_objects()
    return jsonify([obj.to_dict() for obj in objects]), 200

@objects_bp.route('/objects/<int:object_id>', methods=['GET'])
def get_object_by_id(object_id):
    obj = ObjectsService.get_object_by_id(object_id)
    if obj:
        return jsonify(obj.to_dict()), 200
    return jsonify({"message": "Object not found"}), 404

@objects_bp.route('/objects', methods=['POST'])
def create_object():
    data = request.get_json()
    new_object = ObjectsService.create_object(data)
    return jsonify(new_object.to_dict()), 201

@objects_bp.route('/objects/<int:object_id>', methods=['PUT'])
def update_object(object_id):
    data = request.get_json()
    updated_object = ObjectsService.update_object(object_id, data)
    if updated_object:
        return jsonify(updated_object.to_dict()), 200
    return jsonify({"message": "Object not found"}), 404

@objects_bp.route('/objects/<int:object_id>', methods=['DELETE'])
def delete_object(object_id):
    deleted_object = ObjectsService.delete_object(object_id)
    if deleted_object:
        return jsonify({"message": "Object deleted"}), 200
    return jsonify({"message": "Object not found"}), 404
