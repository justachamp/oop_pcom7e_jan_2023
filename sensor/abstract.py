from abc import ABC, abstractmethod


class SensorABC(ABC):
    @abstractmethod
    def collect_data(self):
        pass

    @abstractmethod
    def process_data(self):
        pass

    @abstractmethod
    def get_data(self):
        pass
