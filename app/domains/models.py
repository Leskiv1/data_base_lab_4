# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Index, Integer, String, Table, Text, Date
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import MEDIUMTEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Objects(Base):
    __tablename__ = 'Objects'

    id = Column(Integer, primary_key=True)
    object_name = Column(String(25), nullable=False)
    location = Column(String(225), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'object_name': self.object_name,
            'location': self.location
        }


class Operators(Base):
    __tablename__ = 'Operators'

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    phone = Column(String(45), nullable=False)
    shift_start = Column(DateTime)
    shift_end = Column(DateTime)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'last_name': self.last_name,
            'phone': self.phone,
            'shift_start': self.shift_start,
            'shift_end': self.shift_end
        }

class Rooms(Base):
    __tablename__ = 'Rooms'

    id = Column(Integer, primary_key=True)
    Objects_id = Column(ForeignKey('Objects.id'), nullable=False, index=True)
    room_name = Column(String(45), nullable=False)
    room_number = Column(String(45), nullable=False, index=True)
    room_type = Column(String(45))
    area = Column(String(10))

    def to_dict(self):
        return {
            'id': self.id,
            'Objects_id': self.Objects_id,
            'room_name': self.room_name,
            'room_number': self.room_number,
            'room_type': self.room_type,
            'area': self.area
        }

    Objects = relationship('Objects')
    Zoness = relationship('Zones', secondary='Zones_has_Rooms')
    Sensors = relationship('Sensors', secondary='SensorRoom', back_populates='Rooms')


class Zones(Base):
    __tablename__ = 'Zones'

    id = Column(Integer, primary_key=True)
    Objects_id = Column(ForeignKey('Objects.id'), nullable=False, index=True)
    zone_number = Column(Integer, nullable=False, index=True)
    zone_name = Column(String(45), nullable=False)

    Objects = relationship('Objects')


class AccessLevels(Base):
    __tablename__ = 'Access_Levels'

    id = Column(Integer, primary_key=True)
    Zones_id = Column(ForeignKey('Zones.id'), nullable=False, index=True)
    degree_levels = Column(String(45), nullable=False)
    description = Column(MEDIUMTEXT)

    Zones = relationship('Zones')


class Sensors(Base):
    __tablename__ = 'Sensors'

    id = Column(Integer, primary_key=True)
    Rooms_id = Column(ForeignKey('Rooms.id'), nullable=False, index=True)
    sensor_type = Column(String(45), nullable=False, index=True)
    status = Column(String(45))

    Rooms = relationship('Rooms')
    Rooms = relationship('Rooms', secondary='SensorRoom', back_populates='Sensors')


t_Zones_has_Rooms = Table(
    'Zones_has_Rooms', metadata,
    Column('Zones_id', ForeignKey('Zones.id'), primary_key=True, nullable=False, index=True),
    Column('Rooms_id', ForeignKey('Rooms.id'), primary_key=True, nullable=False, index=True),
    Index('Prime', 'Zones_id', 'Rooms_id')
)


class SensorNotifications(Base):
    __tablename__ = 'Sensor_Notifications'

    id = Column(Integer, primary_key=True)
    Sensors_id = Column(ForeignKey('Sensors.id'), nullable=False, index=True)
    notification_time = Column(DateTime)
    massage = Column(String(45))
    status = Column(String(45))

    Sensors = relationship('Sensors')


class Users(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    Access_Levels_id = Column(ForeignKey('Access_Levels.id'), nullable=False, index=True)
    user_name = Column(String(45), nullable=False)
    position = Column(String(45), nullable=False, index=True)
    user_last_name = Column(String(45))
    user_phone_number = Column(String(45), unique=True)

    Access_Levels = relationship('AccessLevels')


class ProcessedNotification(Base):
    __tablename__ = 'Processed_Notification'

    id = Column(Integer, primary_key=True)
    Operators_id = Column(ForeignKey('Operators.id'), nullable=False, index=True)
    Sensor_Notifications_id = Column(ForeignKey('Sensor_Notifications.id'), nullable=False, index=True)
    decoding_notification = Column(MEDIUMTEXT)
    processing_time = Column(DateTime)

    Operators = relationship('Operators')
    Sensor_Notifications = relationship('SensorNotifications')


class UsersHasProcessedNotification(Base):
    __tablename__ = 'Users_has_Processed_Notification'

    Users_id = Column(ForeignKey('Users.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, index=True)
    Processed_Notification_id = Column(ForeignKey('Processed_Notification.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, index=True)
    delivered = Column(String(10))
    read = Column(String(10))

    Processed_Notification = relationship('ProcessedNotification')
    Users = relationship('Users')

t_SensorRoom = Table(
    'SensorRoom', Base.metadata,
    Column('sensor_id', ForeignKey('Sensors.id'), primary_key=True, nullable=False),
    Column('room_id', ForeignKey('Rooms.id'), primary_key=True, nullable=False)
)