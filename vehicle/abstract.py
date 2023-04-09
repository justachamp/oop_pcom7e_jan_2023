from abc import ABC, abstractmethod


class VehicleABC(ABC):
    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def decelerate(self):
        pass

    @abstractmethod
    def steer(self, direction):
        pass

    @abstractmethod
    def update_location(self):
        pass
