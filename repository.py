from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapper, Session, relationship

import exceptions
from car import CarDTO, WheelDTO, CarRepository, Car
from hm import HeatMapDTO, HeatMapRepository, HeatMap

metadata = MetaData()


heat_map_t = Table(
    'heat_map',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('image_path', String(50)),
    Column('name', String(50)),
)

HeatMapMapper = mapper(
    HeatMapDTO,
    heat_map_t,
    properties={
        'id': heat_map_t.c.id,
        'image_path': heat_map_t.c.image_path,
        'name': heat_map_t.c.name
    }
)


class ORMHeatMapRepository(HeatMapRepository):

    def __init__(self, session: Session):
        self._session = session
        self._query = self._session.query(HeatMapMapper)

    def get(self, heat_map_id) -> HeatMap:
        dto = self._query.filter_by(id=heat_map_id).one_or_none()
        if not dto:
            raise exceptions.NotFound(heat_map_id)
        return HeatMap(dto)

    def save(self, heat_map: HeatMap) -> None:
        self._session.add(heat_map.dto)
        self._session.flush()

    def delete(self, heat_map: HeatMap) -> None:
        self._session.delete(heat_map.dto)
        self._session.flush()


metadata = MetaData()


wheel_t = Table(
    'wheel',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('car_id', String(50), ForeignKey('car.id')),
    Column('status', String(50))
)

car_t = Table(
    'car',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('color', String(50)),
)

mapper(WheelDTO, wheel_t)

CarMapper = mapper(
    CarDTO,
    car_t,
    properties={
        'id': car_t.c.id,
        'color': car_t.c.color,
        'wheels': relationship(WheelDTO, backref='car', order_by=wheel_t.c.id, cascade="all, delete, delete-orphan")
    }
)


class ORMCarRepository(CarRepository):

    def __init__(self, session: Session):
        self._session = session
        self._query = self._session.query(CarMapper)

    def get(self, car_id) -> Car:
        dto = self._query.filter_by(id=car_id).one_or_none()
        if not dto:
            raise exceptions.NotFound(car_id)
        return Car(dto)

    def save(self, car: Car) -> None:
        self._session.add(car.dto)
        self._session.flush()

    def delete(self, car: Car) -> None:
        self._session.delete(car.dto)
        self._session.flush()
