import logging

from .abstract import SensorABC
from shared.data_generator import generate_camera_data

logger = logging.getLogger("root")


class Camera(SensorABC):
    def __init__(self):
        self.data = None
        logger.info('Camera initialized')

    def collect_data(self):
        # collect data from camera
        self.data = generate_camera_data(5)  # example camera data
        logger.info('Camera data collected')

    def process_data(self):
        # process collected data
        self.data = [d * 2 for d in self.data]  # example data processing
        logger.info('Camera data processed')

    def get_data(self):
        # return processed data
        return self.data

    def __repr__(self):
        return 'Camera Sensor'
