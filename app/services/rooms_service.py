from app.dao.rooms_dao import RoomsDAO


class RoomsService:
    @staticmethod
    def get_all_rooms():
        return RoomsDAO.get_all()

    @staticmethod
    def get_room_by_id(room_id):
        return RoomsDAO.get_by_id(room_id)

    @staticmethod
    def create_room(room_data):
        return RoomsDAO.create(room_data)

    @staticmethod
    def update_room(room_id, updated_data):
        return RoomsDAO.update(room_id, updated_data)

    @staticmethod
    def delete_room(room_id):
        return RoomsDAO.delete(room_id)

    @staticmethod
    def get_rooms_by_object(object_id):
        return RoomsDAO.get_rooms_by_object_id(object_id)

    @staticmethod
    def get_all_rooms_with_zones():
        return RoomsDAO.get_all_rooms_with_zones()