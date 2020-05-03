from abc import ABC, abstractmethod


class CarDTO:
    id: int
    color: str
    wheels: list
    fuel: str
    power: str
    speed: str
    avg_consume: str


class WheelDTO:
    id:  int
    car_id: int
    status: str


class Car(object):

    @property
    def color(self) -> str:
        return self.dto.color

    @property
    def data_sheet(self):
        return self.DataSheet(self.dto)

    @property
    def wheels(self) -> list:
        return [self.Wheel(wheel_dto) for wheel_dto in self.dto.wheels]

    def drop_wheel(self, wheel_id: int):
        self.dto.wheels = [dto_wheel for dto_wheel in self.dto.wheels if dto_wheel.id != wheel_id]

    def add_wheel(self, wheel: WheelDTO):
        self.dto.wheels.append(wheel)

    def __init__(self, dto: CarDTO) -> None:
        self.id = dto.id
        self.dto = dto

    class DataSheet(object):

        @property
        def fuel(self):
            return self.dto.fuel

        @property
        def power(self):
            return self.dto.power

        @property
        def speed(self):
            return self.dto.speed

        @property
        def avg_consume(self):
            return self.dto.avg_consume

        def __init__(self, dto: CarDTO):
            self.dto = dto

    class Wheel(object):

        @property
        def status(self):
            return self.dto.status

        def __init__(self, dto):
            self.id = dto.id
            self.dto = dto


class CarRepository(ABC):

    @abstractmethod
    def get(self, id) -> Car:
        raise NotImplementedError

    @abstractmethod
    def get_all(self, id) -> list:
        raise NotImplementedError

    @abstractmethod
    def add(self, car: Car) -> None:
        raise NotImplementedError

    @abstractmethod
    def update(self, car: Car) -> None:
        raise NotImplementedError

    @abstractmethod
    def remove(self, car: Car) -> None:
        raise NotImplementedError
