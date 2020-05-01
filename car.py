from abc import ABC, abstractmethod


class CarDTO(object):
    def __init__(self, id, color, wheels):
        self.id = id
        self.color = color
        self.wheels = wheels


class WheelDTO(object):

    def __init__(self, id, car_id, status):
        self.id = id
        self.car_id = car_id
        self.status = status


class Car(object):

    @property
    def color(self) -> str:
        return self.dto.color

    @property
    def wheels(self) -> list:
        return [self.Wheel(wheel_dto) for wheel_dto in self.dto.wheels]

    def drop_wheel(self, wheel_id):
        self.dto.wheels = [dto_wheel for dto_wheel in self.dto.wheels if dto_wheel.id != wheel_id]

    def __init__(self, dto: CarDTO) -> None:
        self.id = dto.id
        self.dto = dto
        self.__wheels = None

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
    def save(self, car: Car) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, car: Car):
        raise NotImplementedError
