import logging

from .abstract import SensorABC
from shared.data_generator import generate_gps_data

logger = logging.getLogger("root")


class GPS(SensorABC):
    def __init__(self):
        self.data = None
        logger.info('GPS sensor initialized')

    def collect_data(self):
        # collect data from GPS
        self.data = generate_gps_data()  # example GPS data
        logger.info('GPS data collected')

    def process_data(self):
        # process collected data
        pass  # no processing needed for GPS data

    def get_data(self):
        # return processed data
        return self.data

    def __repr__(self):
        return 'GPS sensor'
