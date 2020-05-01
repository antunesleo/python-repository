from abc import ABC, abstractmethod


class HeatMapDTO(object):
    def __init__(self, id, image_path, name):
        self.id = id
        self.image_path = image_path
        self.name = name


class HeatMap(object):

    def __init__(self, dto: HeatMapDTO) -> None:
        self.id = dto.id
        self.dto = dto


class HeatMapRepository(ABC):

    @abstractmethod
    def get(self, id) -> HeatMap:
        raise NotImplementedError

    @abstractmethod
    def save(self, heat_map: HeatMap) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, heat_map: HeatMap):
        raise NotImplementedError
