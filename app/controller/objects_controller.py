from flask import Blueprint, jsonify, request
from flasgger import swag_from
from app.services.objects_service import ObjectsService

objects_bp = Blueprint('objects', __name__)

@objects_bp.route('/objects', methods=['GET'])
def get_all_objects():
    """
    Get all objects
    ---
    tags:
      - Objects
    responses:
      200:
        description: List of all objects
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              object_name:
                type: string
              location:
                type: string
    """
    objects = ObjectsService.get_all_objects()
    return jsonify([obj.to_dict() for obj in objects]), 200

@objects_bp.route('/objects/<int:object_id>', methods=['GET'])
def get_object_by_id(object_id):
    """
    Get object by ID
    ---
    tags:
      - Objects
    parameters:
      - name: object_id
        in: path
        type: integer
        required: true
        description: The object ID
    responses:
      200:
        description: Object details
        schema:
          type: object
          properties:
            id:
              type: integer
            object_name:
              type: string
            location:
              type: string
      404:
        description: Object not found
    """
    obj = ObjectsService.get_object_by_id(object_id)
    if obj:
        return jsonify(obj.to_dict()), 200
    return jsonify({"message": "Object not found"}), 404

@objects_bp.route('/objects', methods=['POST'])
def create_object():
    """
    Create a new object
    ---
    tags:
      - Objects
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - object_name
            - location
          properties:
            object_name:
              type: string
              example: Building A
            location:
              type: string
              example: 123 Main Street, City
    responses:
      201:
        description: Object created successfully
        schema:
          type: object
          properties:
            id:
              type: integer
            object_name:
              type: string
            location:
              type: string
    """
    data = request.get_json()
    new_object = ObjectsService.create_object(data)
    return jsonify(new_object.to_dict()), 201

@objects_bp.route('/objects/<int:object_id>', methods=['PUT'])
def update_object(object_id):
    """
    Update an object
    ---
    tags:
      - Objects
    parameters:
      - name: object_id
        in: path
        type: integer
        required: true
        description: The object ID
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            object_name:
              type: string
            location:
              type: string
    responses:
      200:
        description: Object updated successfully
        schema:
          type: object
          properties:
            id:
              type: integer
            object_name:
              type: string
            location:
              type: string
      404:
        description: Object not found
    """
    data = request.get_json()
    updated_object = ObjectsService.update_object(object_id, data)
    if updated_object:
        return jsonify(updated_object.to_dict()), 200
    return jsonify({"message": "Object not found"}), 404

@objects_bp.route('/objects/<int:object_id>', methods=['DELETE'])
def delete_object(object_id):
    """
    Delete an object
    ---
    tags:
      - Objects
    parameters:
      - name: object_id
        in: path
        type: integer
        required: true
        description: The object ID
    responses:
      200:
        description: Object deleted successfully
        schema:
          type: object
          properties:
            message:
              type: string
      404:
        description: Object not found
    """
    deleted_object = ObjectsService.delete_object(object_id)
    if deleted_object:
        return jsonify({"message": "Object deleted"}), 200
    return jsonify({"message": "Object not found"}), 404
