import logging
import math

from sensor.camera import Camera
from sensor.gps import GPS
from sensor.lidar import Lidar
from .abstract import ControlComputerABC

logger = logging.getLogger("root")


class ControlComputer(ControlComputerABC):
    def __init__(self):
        self.sensors = []
        self.vehicle = None
        logger.info("Control computer initialized")

    def connect_sensor(self, sensor):
        # connect a sensor to the control computer
        self.sensors.append(sensor)
        logger.info(f"Sensor {sensor} connected")

    def connect_vehicle(self, vehicle):
        # connect a vehicle to the control computer
        self.vehicle = vehicle
        logger.info(f"Vehicle {vehicle} connected")

    def process_data(self):
        # process data from all connected sensors
        for sensor in self.sensors:
            sensor.collect_data()
            sensor.process_data()

    def control_vehicle(self):
        # control the connected vehicle based on processed sensor data
        for sensor in self.sensors:
            data = sensor.get_data()
            logger.info(f"Sensor: {sensor}, Data: {data}")
            # example control logic based on camera and Lidar data
            if isinstance(sensor, Camera):
                if any(d > 5 for d in data):
                    self.vehicle.decelerate()
            elif isinstance(sensor, Lidar):
                if all(d < 2 for d in data):
                    self.vehicle.accelerate()
            # example control logic based on GPS data
            elif isinstance(sensor, GPS):
                self.vehicle.steer(math.atan2(data[1], data[0]))

        self.vehicle.update_location()

    def __repr__(self):
        return "ControlComputer"
