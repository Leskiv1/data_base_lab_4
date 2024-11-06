from app.dao.operators_dao import OperatorsDAO


class OperatorsService:
    @staticmethod
    def get_all_operators():
        return OperatorsDAO.get_all()

    @staticmethod
    def get_operator_by_id(operator_id):
        return OperatorsDAO.get_by_id(operator_id)

    @staticmethod
    def create_operator(operator_data):
        return OperatorsDAO.create(operator_data)

    @staticmethod
    def update_operator(operator_id, updated_data):
        return OperatorsDAO.update(operator_id, updated_data)

    @staticmethod
    def delete_operator(operator_id):
        return OperatorsDAO.delete(operator_id)
