from unittest import TestCase
import math

from vehicle.car import Car


class TestCar(TestCase):
    def setUp(self):
        self.car = Car()

    def test_accelerate(self):
        initial_speed = self.car.speed
        self.car.accelerate()
        self.assertGreater(self.car.speed, initial_speed)

    def test_decelerate(self):
        initial_speed = self.car.speed
        self.car.decelerate()
        self.assertLess(self.car.speed, initial_speed)

    def test_steer(self):
        initial_direction = self.car.direction
        self.car.steer(math.pi / 4)
        self.assertNotEqual(self.car.direction, initial_direction)

    def test_update_location(self):
        initial_location = self.car.location
        self.car.speed = 1
        self.car.direction = math.pi / 2
        self.car.update_location()
        expected_location = (initial_location[0] + self.car.speed * math.cos(self.car.direction),
                             initial_location[1] + self.car.speed * math.sin(self.car.direction))
        self.assertEqual(self.car.location, expected_location)
