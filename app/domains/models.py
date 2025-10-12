# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Index, Integer, String, Table, Text
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
    operator_name = Column(String(45), nullable=False)
    operator_last_name = Column(String(45), nullable=False)
    shift_start = Column(DateTime, nullable=False)
    shift_end = Column(DateTime, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.operator_name,
            'last_name': self.operator_last_name,
            'phone': None,  # Phone is in OperatorDetails
            'shift_start': self.shift_start.isoformat() if self.shift_start else None,
            'shift_end': self.shift_end.isoformat() if self.shift_end else None
        }


class Zones(Base):
    __tablename__ = 'Zones'

    id = Column(Integer, primary_key=True)
    object_id = Column(ForeignKey('Objects.id'), nullable=False, index=True)
    zone_number = Column(Integer, nullable=False, index=True)
    zone_name = Column(String(45), nullable=False)

    Objects = relationship('Objects')


class Rooms(Base):
    __tablename__ = 'Rooms'

    id = Column(Integer, primary_key=True)
    object_id = Column(ForeignKey('Objects.id'), nullable=False, index=True)
    room_name = Column(String(45), nullable=False)
    room_number = Column(String(45), nullable=False, index=True)
    room_type = Column(String(45))
    area = Column(String(10))

    def to_dict(self):
        return {
            'id': self.id,
            'Objects_id': self.object_id,  # Keep API consistent
            'room_name': self.room_name,
            'room_number': self.room_number,
            'room_type': self.room_type,
            'area': self.area
        }

    Objects = relationship('Objects')
    Zoness = relationship('Zones', secondary='Zones_has_Rooms')
    Sensors = relationship('Sensors', back_populates='Rooms')


t_Zones_has_Rooms = Table(
    'Zones_has_Rooms', metadata,
    Column('zone_id', ForeignKey('Zones.id'), primary_key=True, nullable=False),
    Column('room_id', ForeignKey('Rooms.id'), primary_key=True, nullable=False)
)


class AccessLevels(Base):
    __tablename__ = 'Access_Levels'

    id = Column(Integer, primary_key=True)
    zone_id = Column(ForeignKey('Zones.id'), nullable=False, index=True)
    degree_levels = Column(String(45), nullable=False)
    description = Column(MEDIUMTEXT)

    Zones = relationship('Zones')


class Users(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    access_level_id = Column(ForeignKey('Access_Levels.id'), unique=True)
    position = Column(String(45), nullable=False, index=True)
    user_name = Column(String(45), nullable=False)
    user_last_name = Column(String(45), nullable=False)

    Access_Levels = relationship('AccessLevels')


class Sensors(Base):
    __tablename__ = 'Sensors'

    id = Column(Integer, primary_key=True)
    room_id = Column(ForeignKey('Rooms.id'), nullable=False, index=True)
    sensor_type = Column(String(45), nullable=False, index=True)
    status = Column(String(45))

    Rooms = relationship('Rooms', back_populates='Sensors')


class SensorNotifications(Base):
    __tablename__ = 'Sensor_Notifications'

    id = Column(Integer, primary_key=True)
    sensor_id = Column(ForeignKey('Sensors.id'), nullable=False, index=True)
    notification_time = Column(DateTime, nullable=False)
    message = Column(String(45), nullable=False)
    status = Column(String(45), nullable=False)

    Sensors = relationship('Sensors')


class ProcessedNotification(Base):
    __tablename__ = 'Processed_Notification'

    id = Column(Integer, primary_key=True)
    operator_id = Column(ForeignKey('Operators.id'), nullable=False, index=True)
    sensor_notification_id = Column(ForeignKey('Sensor_Notifications.id'), unique=True, nullable=False)
    decoding_notification = Column(MEDIUMTEXT, nullable=False)
    processing_time = Column(DateTime, nullable=False)

    Operators = relationship('Operators')
    Sensor_Notifications = relationship('SensorNotifications')


class UsersHasProcessedNotification(Base):
    __tablename__ = 'Users_has_Processed_Notification'

    user_id = Column(ForeignKey('Users.id'), primary_key=True, nullable=False)
    processed_notification_id = Column(ForeignKey('Processed_Notification.id'), primary_key=True, nullable=False)
    delivered = Column(String(10), nullable=False)
    readed = Column(String(10), nullable=False)

    Processed_Notification = relationship('ProcessedNotification')
    Users = relationship('Users')