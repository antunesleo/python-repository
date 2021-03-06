from abc import ABC, abstractmethod


class HeatMapDTO(object):
    def __init__(self, id, image_path, name):
        self.id = id
        self.image_path = image_path
        self.name = name


class HeatMap(object):

    @property
    def image_path(self) -> str:
        return self.dto.image_path

    @property
    def name(self) -> str:
        return self.dto.name

    def __init__(self, dto: HeatMapDTO) -> None:
        self.id = dto.id
        self.dto = dto


class HeatMapRepository(ABC):

    @abstractmethod
    def get(self, id) -> HeatMap:
        raise NotImplementedError

    @abstractmethod
    def get_all(self, id) -> list:
        raise NotImplementedError

    @abstractmethod
    def add(self, heat_map: HeatMap) -> None:
        raise NotImplementedError

    @abstractmethod
    def update(self, heat_map: HeatMap) -> None:
        raise NotImplementedError

    @abstractmethod
    def remove(self, heat_map: HeatMap) -> None:
        raise NotImplementedError
