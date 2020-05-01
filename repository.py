from sqlalchemy import Table, MetaData, Column, Integer, String
from sqlalchemy.orm import mapper, Session

import exceptions
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
