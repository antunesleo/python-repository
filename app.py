from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import exceptions
from hm import HeatMapDTO, HeatMap
from repository import ORMHeatMapRepository

session = None


def prepare_repository():
    some_engine = create_engine('sqlite:///repo-adventures.db')
    SessionMaker = sessionmaker(bind=some_engine)
    session = SessionMaker()
    return ORMHeatMapRepository(session)


def commit():
    session.commit()


if __name__ == '__main__':
    heat_map_repository = prepare_repository()

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

    commit()
