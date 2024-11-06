from flask import Blueprint, jsonify, request
from app.services.operators_service import OperatorsService

operators_bp = Blueprint('operators', __name__)

@operators_bp.route('/operators', methods=['GET'])
def get_all_operators():
    operators = OperatorsService.get_all_operators()
    return jsonify([operator.to_dict() for operator in operators]), 200

@operators_bp.route('/operators/<int:operator_id>', methods=['GET'])
def get_operator_by_id(operator_id):
    operator = OperatorsService.get_operator_by_id(operator_id)
    if operator:
        return jsonify(operator.to_dict()), 200
    return jsonify({"message": "Operator not found"}), 404

@operators_bp.route('/operators', methods=['POST'])
def create_operator():
    data = request.get_json()
    new_operator = OperatorsService.create_operator(data)
    return jsonify(new_operator.to_dict()), 201

@operators_bp.route('/operators/<int:operator_id>', methods=['PUT'])
def update_operator(operator_id):
    data = request.json
    updated_operator = OperatorsService.update_operator(operator_id, data)
    if updated_operator:
        return jsonify(updated_operator.to_dict()), 200
    return jsonify({"message": "Operator not found"}), 404

@operators_bp.route('/operators/<int:operator_id>', methods=['DELETE'])
def delete_operator(operator_id):
    deleted_operator = OperatorsService.delete_operator(operator_id)
    if deleted_operator:
        return jsonify({"message": "Operator deleted"}), 200
    return jsonify({"message": "Operator not found"}), 404
