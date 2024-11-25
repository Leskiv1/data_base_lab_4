from flask import Blueprint, request, jsonify
from app import db
from app.dao.sensor_maintenance_dao import SensorDAO
from app.services.sensor_maintenance_service import SensorService

sensor_bp = Blueprint('sensor', __name__)

sensor_dao = SensorDAO(db)
sensor_service = SensorService(sensor_dao)


@sensor_bp.route('/sensors/sensor/maintenance', methods=['POST'])
def insert_sensor_maintenance():
    data = request.get_json()
    sensor_id = data['sensor_id']
    maintenance_date = data['maintenance_date']
    details = data['details']

    try:
        # Викликаємо DAO метод для вставки даних
        sensor_service.insert_sensor_maintenance(sensor_id, maintenance_date, details)
        return jsonify({'message': 'Sensor maintenance record inserted!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@sensor_bp.route('/sensor/room', methods=['POST'])
def insert_sensor_room_connection():
    data = request.get_json()

    # Отримання sensor_type і room_name з JSON-запиту
    sensor_type = data['sensor_type']
    room_name = data['room_name']

    # Виклик сервісу для вставки зв'язку між сенсором та кімнатою
    sensor_service.insert_sensor_room_connection(sensor_type, room_name)

    return jsonify({'message': 'Sensor-room connection created!'}), 201


@sensor_bp.route('/sensor/maintenance/multiple', methods=['POST'])
def insert_multiple_maintenance():
    data = request.get_json()
    sensor_id = data['sensor_id']

    sensor_service.insert_multiple_maintenance(sensor_id)
    return jsonify({'message': 'Multiple maintenance records inserted!'}), 201



@sensor_bp.route('/sensor/maintenance/avg_length', methods=['GET'])
def get_avg_maintenance_length():
    # Викликаємо DAO метод для отримання середнього значення довжини
    result = sensor_service.get_avg_maintenance_length()
    if result is not None:
        # Перетворюємо Decimal в float перед відправкою в JSON
        return jsonify({'avg_maintenance_length': float(result)}), 200
    else:
        return jsonify({'error': 'No data found'}), 404


@sensor_bp.route('/sensor/tables/random', methods=['POST'])
def create_random_sensor_tables():
    result = sensor_service.create_random_sensor_tables()
    if result:
        return jsonify({'message': 'Random sensor tables created!'}), 201
    else:
        return jsonify({"message": 'Error while creating sensor tables'}), 404

