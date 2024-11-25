from sqlalchemy import text
class SensorDAO:
    def __init__(self, db):
        self.db = db

    def insert_sensor_maintenance(self, sensor_id, maintenance_date, details):
        # Використовуємо SQLAlchemy для виконання збереженої процедури
        query = text("CALL insert_sensor_maintenance(:sensor_id, :maintenance_date, :details)")
        self.db.session.execute(query, {'sensor_id': sensor_id, 'maintenance_date': maintenance_date, 'details': details})
        self.db.session.commit()

    def insert_sensor_room_connection(self, sensor_type, room_name):
        query = text("CALL insert_sensor_room_connection(:sensor_type, :room_name)")
        self.db.session.execute(query, {'sensor_type': sensor_type, 'room_name': room_name})
        self.db.session.commit()

    def insert_multiple_maintenance(self, sensor_id):
        query = text("CALL insert_multiple_maintenance(:sensor_id)")
        self.db.session.execute(query, {"sensor_id": sensor_id})
        self.db.session.commit()

    def get_avg_maintenance_length(self):
        # Викликаємо функцію get_avg_maintenance_length
        query = text("SELECT get_avg_maintenance_length()")
        result = self.db.session.execute(query).scalar()  # .scalar() повертає єдине значення

        # Закриваємо сесію після виконання запиту
        self.db.session.close()

        # Повертаємо отриманий результат (Decimal)
        return result

    def create_random_sensor_tables(self):
        try:
            # Виконання процедури
            query = text("CALL create_random_sensor_tables()")
            self.db.session.execute(query)
            self.db.session.commit()  # Фіксуємо зміни
            return True
        except Exception as e:
            print(f"Error in DAO: {e}")
            self.db.session.rollback()  # Відкат у разі помилки
            return False



