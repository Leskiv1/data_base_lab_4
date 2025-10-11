from flask import Blueprint, jsonify, request
from flasgger import swag_from
from app.services.operators_service import OperatorsService

operators_bp = Blueprint('operators', __name__)

@operators_bp.route('/operators', methods=['GET'])
def get_all_operators():
    """
    Get all operators
    ---
    tags:
      - Operators
    responses:
      200:
        description: List of all operators
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              name:
                type: string
              last_name:
                type: string
              phone:
                type: string
              shift_start:
                type: string
                format: date-time
              shift_end:
                type: string
                format: date-time
    """
    operators = OperatorsService.get_all_operators()
    return jsonify([operator.to_dict() for operator in operators]), 200

@operators_bp.route('/operators/<int:operator_id>', methods=['GET'])
def get_operator_by_id(operator_id):
    """
    Get operator by ID
    ---
    tags:
      - Operators
    parameters:
      - name: operator_id
        in: path
        type: integer
        required: true
        description: The operator ID
    responses:
      200:
        description: Operator details
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            last_name:
              type: string
            phone:
              type: string
            shift_start:
              type: string
              format: date-time
            shift_end:
              type: string
              format: date-time
      404:
        description: Operator not found
    """
    operator = OperatorsService.get_operator_by_id(operator_id)
    if operator:
        return jsonify(operator.to_dict()), 200
    return jsonify({"message": "Operator not found"}), 404

@operators_bp.route('/operators', methods=['POST'])
def create_operator():
    """
    Create a new operator
    ---
    tags:
      - Operators
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - name
            - last_name
            - phone
          properties:
            name:
              type: string
              example: John
            last_name:
              type: string
              example: Doe
            phone:
              type: string
              example: "+1234567890"
            shift_start:
              type: string
              format: date-time
              example: "2024-01-01T08:00:00"
            shift_end:
              type: string
              format: date-time
              example: "2024-01-01T16:00:00"
    responses:
      201:
        description: Operator created successfully
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            last_name:
              type: string
            phone:
              type: string
            shift_start:
              type: string
              format: date-time
            shift_end:
              type: string
              format: date-time
    """
    data = request.get_json()
    new_operator = OperatorsService.create_operator(data)
    return jsonify(new_operator.to_dict()), 201

@operators_bp.route('/operators/<int:operator_id>', methods=['PUT'])
def update_operator(operator_id):
    """
    Update an operator
    ---
    tags:
      - Operators
    parameters:
      - name: operator_id
        in: path
        type: integer
        required: true
        description: The operator ID
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            last_name:
              type: string
            phone:
              type: string
            shift_start:
              type: string
              format: date-time
            shift_end:
              type: string
              format: date-time
    responses:
      200:
        description: Operator updated successfully
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            last_name:
              type: string
            phone:
              type: string
            shift_start:
              type: string
              format: date-time
            shift_end:
              type: string
              format: date-time
      404:
        description: Operator not found
    """
    data = request.json
    updated_operator = OperatorsService.update_operator(operator_id, data)
    if updated_operator:
        return jsonify(updated_operator.to_dict()), 200
    return jsonify({"message": "Operator not found"}), 404

@operators_bp.route('/operators/<int:operator_id>', methods=['DELETE'])
def delete_operator(operator_id):
    """
    Delete an operator
    ---
    tags:
      - Operators
    parameters:
      - name: operator_id
        in: path
        type: integer
        required: true
        description: The operator ID
    responses:
      200:
        description: Operator deleted successfully
        schema:
          type: object
          properties:
            message:
              type: string
      404:
        description: Operator not found
    """
    deleted_operator = OperatorsService.delete_operator(operator_id)
    if deleted_operator:
        return jsonify({"message": "Operator deleted"}), 200
    return jsonify({"message": "Operator not found"}), 404
