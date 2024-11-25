class SensorService:
    def __init__(self, sensor_dao):
        self.sensor_dao = sensor_dao

    def insert_sensor_maintenance(self, sensor_id, maintenance_date, details):
        self.sensor_dao.insert_sensor_maintenance(sensor_id, maintenance_date, details)

    def insert_sensor_room_connection(self, sensor_name, room_name):
        self.sensor_dao.insert_sensor_room_connection(sensor_name, room_name)

    def insert_multiple_maintenance(self, sensor_id):
        self.sensor_dao.insert_multiple_maintenance(sensor_id)

    def get_avg_maintenance_length(self):
        return self.sensor_dao.get_avg_maintenance_length()

    def create_random_sensor_tables(self):
        return self.sensor_dao.create_random_sensor_tables()


