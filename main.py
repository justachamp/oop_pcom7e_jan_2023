import logging

from control_computer.control_computer import ControlComputer
from sensor.camera import Camera
from sensor.gps import GPS
from sensor.lidar import Lidar
from vehicle.car import Car

formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger = logging.getLogger("root")
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

if __name__ == '__main__':
    car = Car()
    camera = Camera()
    lidar = Lidar()
    gps = GPS()

    logger.info('Starting the vehicle control computer')
    computer = ControlComputer()
    logger.info('Connecting to the vehicle')
    computer.connect_vehicle(car)
    logger.info('Connecting to the sensors')
    computer.connect_sensor(camera)
    computer.connect_sensor(lidar)
    computer.connect_sensor(gps)
    logger.info('Finished connecting to the sensors')
    logger.info('Starting the vehicle')
    while True:
        computer.process_data()
        computer.control_vehicle()
