import unittest

from sensor.gps import GPS


class TestGPS(unittest.TestCase):

    def test_collect_data(self):
        gps = GPS()
        gps.collect_data()
        self.assertIsNotNone(gps.data)

    def test_process_data(self):
        gps = GPS()
        gps.data = (37.7749, -122.4194)
        gps.process_data()
        self.assertIsNotNone(gps.data)

    def test_get_data(self):
        gps = GPS()
        gps.data = (37.7749, -122.4194)
        self.assertEqual(gps.get_data(), (37.7749, -122.4194))