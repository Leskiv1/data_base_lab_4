from app.domains.models import Rooms, Zones
from app import db
from sqlalchemy.orm import joinedload


class RoomsDAO:
    @staticmethod
    def get_all():
        return db.session.query(Rooms).all()

    @staticmethod
    def get_by_id(room_id):
        return db.session.query(Rooms).get(room_id)

    @staticmethod
    def create(room_data):
        new_room = Rooms(**room_data)
        db.session.add(new_room)
        db.session.commit()
        return new_room

    @staticmethod
    def update(room_id, updated_data):
        room_to_update = RoomsDAO.get_by_id(room_id)
        if room_to_update:
            for key, value in updated_data.items():
                setattr(room_to_update, key, value)
            db.session.commit()
        return room_to_update

    @staticmethod
    def delete(room_id):
        room_to_delete = RoomsDAO.get_by_id(room_id)
        if room_to_delete:
            db.session.delete(room_to_delete)
            db.session.commit()
        return room_to_delete

    @staticmethod
    def get_rooms_by_object_id(object_id):
        return db.session.query(Rooms).filter_by(Objects_id=object_id).all()

    @staticmethod
    def get_all_rooms_with_zones():
        return db.session.query(Rooms).options(joinedload(Rooms.Zoness)).all()


