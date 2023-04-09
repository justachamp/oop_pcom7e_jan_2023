from abc import ABC, abstractmethod


class ControlComputerABC(ABC):
    @abstractmethod
    def connect_sensor(self, sensor):
        pass

    @abstractmethod
    def connect_vehicle(self, vehicle):
        pass

    @abstractmethod
    def process_data(self):
        pass

    @abstractmethod
    def control_vehicle(self):
        pass
