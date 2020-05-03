from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapper, Session, relationship

import exceptions
from domain.car import CarDTO, WheelDTO, CarRepository, Car


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
    Column('fuel', String(50)),
    Column('power', String(50)),
    Column('speed', String(50)),
    Column('avg_consume', String(50)),
)

mapper(WheelDTO, wheel_t)

CarMapper = mapper(
    CarDTO,
    car_t,
    properties={
        'id': car_t.c.id,
        'color': car_t.c.color,
        'fuel': car_t.c.fuel,
        'power': car_t.c.power,
        'speed': car_t.c.speed,
        'avg_consume': car_t.c.avg_consume,
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

    def get_all(self, car_id) -> list:
        return [Car(dto) for dto in self._query.filter()]

    def add(self, car: Car) -> None:
        self._session.add(car.dto)
        self._session.flush()

    def update(self, car: Car) -> None:
        self._session.add(car.dto)
        self._session.flush()

    def remove(self, car: Car) -> None:
        self._session.delete(car.dto)
        self._session.flush()
