from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import exceptions
from domain.car import WheelDTO
from domain.hm import HeatMapDTO, HeatMap
from repository.car import ORMCarRepository
from repository.hm import ORMHeatMapRepository


if __name__ == '__main__':
    some_engine = create_engine('sqlite:///repo-adventures.db')
    SessionMaker = sessionmaker(bind=some_engine)
    session = SessionMaker()
    heat_map_repository = ORMHeatMapRepository(session)

    heat_map = heat_map_repository.get(1)
    assert heat_map.dto.name == 'An awesome map!'

    heat_map_dto = HeatMapDTO(4, 'some_path', 'The forth awesome map')
    heat_map = HeatMap(heat_map_dto)
    heat_map_repository.save(heat_map)
    assert heat_map_repository.get(4).dto.name == 'The forth awesome map'
    heat_map.dto.name = 'I have changed my mind'
    heat_map_repository.save(heat_map)
    assert heat_map_repository.get(4).dto.name == 'I have changed my mind'

    heat_map.dto.name = 'fpadskpfpsfdkpasfsadpfpasd'
    heat_map_repository.delete(heat_map)
    try:
        heat_map_repository.get(4)
        assert False
    except exceptions.NotFound:
        pass

    car_repository = ORMCarRepository(session)
    car = car_repository.get(1)
    assert car.color == 'red'
    assert len(car.wheels) == 4
    assert isinstance(car.wheels, list)
    assert isinstance(car.data_sheet, car.DataSheet)
    car.drop_wheel(4)
    assert len(car.wheels) == 3
    car_repository.save(car)
    recent_car = car_repository.get(1)
    assert len(recent_car.wheels) == 3

    wheel_dto = WheelDTO()
    wheel_dto.id = 5
    wheel_dto.car_id = 1
    wheel_dto.status = 'broken'
    car.add_wheel(wheel_dto)
    car_repository.save(car)

    # Uncomment if you want to persist it
    # session.commit()
