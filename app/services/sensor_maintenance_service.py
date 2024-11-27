class SensorService:
    def __init__(self, sensor_dao):
        self.sensor_dao = sensor_dao

    def insert_into_table(self, table_name, column_names, values_list):
        self.sensor_dao.insert_into_table(table_name, column_names, values_list)

    def insert_zone_room_association(self, room_name, zone_name):
        self.sensor_dao.insert_zone_room_association(room_name, zone_name)

    def insert_multiple_maintenance(self, sensor_id):
        self.sensor_dao.insert_multiple_maintenance(sensor_id)

    def get_avg_maintenance_length(self):
        return self.sensor_dao.get_avg_maintenance_length()

    def create_random_sensor_tables(self):
        return self.sensor_dao.create_random_sensor_tables()


