from flask import Blueprint, request, jsonify
from app import db
from app.dao.sensor_maintenance_dao import SensorDAO
from app.services.sensor_maintenance_service import SensorService

sensor_bp = Blueprint('sensor', __name__)

sensor_dao = SensorDAO(db)
sensor_service = SensorService(sensor_dao)

@sensor_bp.route('/table/insert', methods=['POST'])
def insert_into_table():
    data = request.get_json()
    table_name = data['table_name']
    column_names = data['column_names']
    values_list = data['values_list']

    try:
        sensor_service.insert_into_table(table_name, column_names, values_list)
        return jsonify({'message': 'Data inserted successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 50



@sensor_bp.route('/zones/rooms/associate', methods=['POST'])
def insert_zone_room_association():
    data = request.get_json()
    room_name = data['room_name']
    zone_name = data['zone_name']

    try:
        # Викликаємо сервіс для вставки зв'язку між кімнатою і зоною
        sensor_service.insert_zone_room_association(room_name, zone_name)
        return jsonify({'message': 'Room and Zone association created successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500



@sensor_bp.route('/insert/multiple/maintenance', methods=['POST'])
def insert_multiple_maintenance():
    data = request.get_json()
    sensor_id = data['sensor_id']

    sensor_service.insert_multiple_maintenance(sensor_id)
    return jsonify({'message': 'Multiple maintenance records inserted!'}), 201



@sensor_bp.route('/avg_length', methods=['GET'])
def get_avg_maintenance_length():
    # Викликаємо DAO метод для отримання середнього значення довжини
    result = sensor_service.get_avg_maintenance_length()
    if result is not None:
        # Перетворюємо Decimal в float перед відправкою в JSON
        return jsonify({'avg_maintenance_length': float(result)}), 200
    else:
        return jsonify({'error': 'No data found'}), 404


@sensor_bp.route('/tables/random', methods=['POST'])
def create_random_sensor_tables():
    result = sensor_service.create_random_sensor_tables()
    if result:
        return jsonify({'message': 'Random sensor tables created!'}), 201
    else:
        return jsonify({"message": 'Error while creating sensor tables'}), 404

