from flask import Blueprint, jsonify, request
from app.services.rooms_service import RoomsService

rooms_bp = Blueprint('rooms', __name__)

@rooms_bp.route('/rooms', methods=['GET'])
def get_all_rooms():
    rooms = RoomsService.get_all_rooms()
    return jsonify([room.to_dict() for room in rooms]), 200

@rooms_bp.route('/rooms/<int:room_id>', methods=['GET'])
def get_room_by_id(room_id):
    room = RoomsService.get_room_by_id(room_id)
    if room:
        return jsonify(room.to_dict()), 200
    return jsonify({"message": "Room not found"}), 404

@rooms_bp.route('/rooms', methods=['POST'])
def create_room():
    data = request.json
    new_room = RoomsService.create_room(data)
    return jsonify(new_room.to_dict()), 201

@rooms_bp.route('/rooms/<int:room_id>', methods=['PUT'])
def update_room(room_id):
    data = request.json
    updated_room = RoomsService.update_room(room_id, data)
    if updated_room:
        return jsonify(updated_room.to_dict()), 200
    return jsonify({"message": "Room not found"}), 404

@rooms_bp.route('/rooms/<int:room_id>', methods=['DELETE'])
def delete_room(room_id):
    deleted_room = RoomsService.delete_room(room_id)
    if deleted_room:
        return jsonify({"message": "Room deleted"}), 200
    return jsonify({"message": "Room not found"}), 404

@rooms_bp.route('objects/<int:object_id>/rooms', methods=['GET'])
def get_rooms_by_object(object_id):
    rooms = RoomsService.get_rooms_by_object(object_id)
    if rooms:
        return jsonify([room.to_dict() for room in rooms]), 200
    return jsonify({"error": "Rooms not found"}), 404


@rooms_bp.route('/rooms_with_zones', methods=['GET'])
def get_all_zones_and_rooms():
    rooms = RoomsService.get_all_rooms_with_zones()

    # Формування структури JSON для зон з кімнатами
    zones_with_rooms = []
    for room in rooms:
        for zone in room.Zoness:
            zone_entry = next((z for z in zones_with_rooms if z['zone_id'] == zone.id), None)
            if not zone_entry:
                zone_entry = {
                    'zone_id': zone.id,
                    'zone_name': zone.zone_name,
                    'zone_number': zone.zone_number,
                    'Objects_id': zone.Objects_id,
                    # Ініціалізуємо кімнати пустим списком
                    'rooms': []
                }
                zones_with_rooms.append(zone_entry)
            # Додати кімнату до зони
            zone_entry['rooms'].append({
                'room_id': room.id,
                'room_name': room.room_name,
                'room_number': room.room_number,
                'room_type': room.room_type,
                'area': room.area
            })

    # Формування структури JSON для кімнат із зонами
    rooms_with_zones = []
    for room in rooms:
        room_zones = [
            {
                'zone_id': zone.id,
                'zone_name': zone.zone_name,
                'zone_number': zone.zone_number,
                'Objects_id': zone.Objects_id
            }
            for zone in room.Zoness
        ]
        rooms_with_zones.append({
            'room_id': room.id,
            'room_name': room.room_name,
            'room_number': room.room_number,
            'room_type': room.room_type,
            'area': room.area,
            'zones': room_zones
        })

    # Відсортувати zones_with_rooms, щоб rooms були вкінці
    for zone in zones_with_rooms:
        # Зберігаємо кімнати
        rooms_data = zone.pop('rooms', [])
        # Переміщуємо кімнати в кінець
        zone['rooms'] = rooms_data

    # Виводимо результат у JSON
    return jsonify({
        'zones_with_rooms': zones_with_rooms,
        'rooms_with_zones': rooms_with_zones
    }), 200
