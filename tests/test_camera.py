import unittest

from sensor.camera import Camera


class TestCamera(unittest.TestCase):

    def test_collect_data(self):
        camera = Camera()
        camera.collect_data()
        self.assertIsNotNone(camera.data)

    def test_process_data(self):
        camera = Camera()
        camera.data = [1, 2, 3, 4, 5]
        camera.process_data()
        self.assertEqual(camera.data, [2, 4, 6, 8, 10])

    def test_get_data(self):
        camera = Camera()
        camera.data = [1, 2, 3, 4, 5]
        self.assertEqual(camera.get_data(), [1, 2, 3, 4, 5])