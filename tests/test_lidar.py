import unittest

from sensor.lidar import Lidar


class TestLidar(unittest.TestCase):

    def test_collect_data(self):
        lidar = Lidar()
        lidar.collect_data()
        self.assertIsNotNone(lidar.data)

    def test_process_data(self):
        lidar = Lidar()
        lidar.data = [0.5, 1.0, 1.5, 2.0, 2.5]
        lidar.process_data()
        self.assertEqual(lidar.data, [0.25, 1.0, 2.25, 4.0, 6.25])

    def test_get_data(self):
        lidar = Lidar()
        lidar.data = [0.5, 1.0, 1.5, 2.0, 2.5]
        self.assertEqual(lidar.get_data(), [0.5, 1.0, 1.5, 2.0, 2.5])