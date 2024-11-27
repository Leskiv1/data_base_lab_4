from sqlalchemy import text
class SensorDAO:
    def __init__(self, db):
        self.db = db

    def insert_into_table(self, table_name, column_names, values_list):
        # Використовуємо SQLAlchemy для виконання збереженої процедури
        query = text("CALL InsertIntoTable(:table_name, :column_names, :values_list)")
        self.db.session.execute(query, {
            'table_name': table_name,
            'column_names': column_names,
            'values_list': values_list
        })
        self.db.session.commit()

    def insert_zone_room_association(self, room_name, zone_name):
        query = text("CALL InsertZoneRoomAssociation(:room_name, :zone_name)")
        self.db.session.execute(query, {'room_name': room_name, 'zone_name': zone_name})
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



