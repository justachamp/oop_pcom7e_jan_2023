import logging

from .abstract import SensorABC
from shared.data_generator import generate_lidar_data

logger = logging.getLogger("root")


class Lidar(SensorABC):
    def __init__(self):
        self.data = None
        logger.info('Lidar sensor initialized')

    def collect_data(self):
        # collect data from Lidar
        self.data = generate_lidar_data()  # example Lidar data
        logger.info('Lidar data collected')

    def process_data(self):
        # process collected data
        self.data = [d ** 2 for d in self.data]  # example data processing
        logger.info('Lidar data processed')

    def get_data(self):
        # return processed data
        return self.data

    def __repr__(self):
        return 'Lidar sensor'
