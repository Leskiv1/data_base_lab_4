from app.dao.objects_dao import ObjectsDAO


class ObjectsService:
    @staticmethod
    def get_all_objects():
        return ObjectsDAO.get_all()

    @staticmethod
    def get_object_by_id(object_id):
        return ObjectsDAO.get_by_id(object_id)

    @staticmethod
    def create_object(object_data):
        return ObjectsDAO.create(object_data)

    @staticmethod
    def update_object(object_id, updated_data):
        return ObjectsDAO.update(object_id, updated_data)

    @staticmethod
    def delete_object(object_id):
        return ObjectsDAO.delete(object_id)
