from app.domains.models import Operators
from app import db


class OperatorsDAO:
    @staticmethod
    def get_all():
        return db.session.query(Operators).all()

    @staticmethod
    def get_by_id(operator_id):
        return db.session.query(Operators).get(operator_id)

    @staticmethod
    def create(operator_data):
        new_operator = Operators(**operator_data)
        db.session.add(new_operator)
        db.session.commit()
        return new_operator

    @staticmethod
    def update(operator_id, updated_data):
        operator_to_update = OperatorsDAO.get_by_id(operator_id)
        if operator_to_update:
            for key, value in updated_data.items():
                setattr(operator_to_update, key, value)
            db.session.commit()
        return operator_to_update

    @staticmethod
    def delete(operator_id):
        operator_to_delete = OperatorsDAO.get_by_id(operator_id)
        if operator_to_delete:
            db.session.delete(operator_to_delete)
            db.session.commit()
        return operator_to_delete
