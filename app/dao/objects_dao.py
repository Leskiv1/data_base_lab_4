from app.domains.models import Objects
from app import db


class ObjectsDAO:
    @staticmethod
    def get_all():
        return db.session.query(Objects).all()

    @staticmethod
    def get_by_id(object_id):
        return db.session.query(Objects).get(object_id)

    @staticmethod
    def create(object_data):
        new_object = Objects(**object_data)
        db.session.add(new_object)
        db.session.commit()
        return new_object

    @staticmethod
    def update(object_id, updated_data):
        object_to_update = ObjectsDAO.get_by_id(object_id)
        if object_to_update:
            for key, value in updated_data.items():
                setattr(object_to_update, key, value)
            db.session.commit()
        return object_to_update

    @staticmethod
    def delete(object_id):
        object_to_delete = ObjectsDAO.get_by_id(object_id)
        if object_to_delete:
            db.session.delete(object_to_delete)
            db.session.commit()
        return object_to_delete
