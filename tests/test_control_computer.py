import unittest
from unittest.mock import MagicMock

from control_computer import control_computer
from sensor.camera import Camera
from sensor.gps import GPS
from sensor.lidar import Lidar
from vehicle.car import Car


class TestControlComputer(unittest.TestCase):
    def setUp(self):
        self.computer = control_computer.ControlComputer()
        self.car = Car()

    def test_connect_sensor(self):
        sensor = Camera()
        self.computer.connect_sensor(sensor)
        self.assertIn(sensor, self.computer.sensors)

    def test_connect_vehicle(self):
        self.computer.connect_vehicle(self.car)
        self.assertEqual(self.car, self.computer.vehicle)

    def test_process_data(self):
        camera = Camera()
        lidar = Lidar()
        gps = GPS()
        self.computer.connect_sensor(camera)
        self.computer.connect_sensor(lidar)
        self.computer.connect_sensor(gps)
        camera.collect_data = MagicMock()
        camera.process_data = MagicMock()
        lidar.collect_data = MagicMock()
        lidar.process_data = MagicMock()
        gps.collect_data = MagicMock()
        gps.process_data = MagicMock()
        self.computer.process_data()
        camera.collect_data.assert_called_once()
        camera.process_data.assert_called_once()
        lidar.collect_data.assert_called_once()
        lidar.process_data.assert_called_once()
        gps.collect_data.assert_called_once()
        gps.process_data.assert_called_once()

    def test_control_vehicle_camera(self):
        camera = Camera()
        self.computer.connect_sensor(camera)
        self.computer.connect_vehicle(self.car)
        camera.get_data = MagicMock(return_value=[6, 7, 8, 9, 10])
        self.computer.control_vehicle()
        self.assertEqual(self.car.speed, -1)

    def test_control_vehicle_lidar(self):
        lidar = Lidar()
        self.computer.connect_sensor(lidar)
        self.computer.connect_vehicle(self.car)
        lidar.get_data = MagicMock(return_value=[0.5, 1.0, 1.5, 2.0, 2.5])
        self.computer.control_vehicle()
        self.assertEqual(self.car.speed, 0)

    def test_control_vehicle_gps(self):
        gps = GPS()
        self.computer.connect_sensor(gps)
        self.computer.connect_vehicle(self.car)
        gps.get_data = MagicMock(return_value=(0, 1))
        self.computer.control_vehicle()
        self.assertAlmostEqual(self.car.direction, 1.5708, places=4)
