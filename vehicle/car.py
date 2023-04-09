import logging
import math

from vehicle.abstract import VehicleABC

logger = logging.getLogger("root")


class Car(VehicleABC):
    MAX_SPEED = 400

    def __init__(self):
        self.speed = 0
        self.direction = 0
        self.location = (0, 0)
        logger.info("Car created")

    def accelerate(self):
        # increase the speed of the car
        self.speed += 2
        if self.speed > self.MAX_SPEED:
            self.speed = self.MAX_SPEED
        logger.info(f"Accelerating car to {self.speed}")

    def decelerate(self):
        # decrease the speed of the car
        self.speed -= 1
        logger.info(f"Decelerating car to {self.speed}")

    def steer(self, direction):
        # change the direction of the car
        self.direction = direction
        logger.info(f"Steering car to {direction}")

    def update_location(self):
        # calculate the new location of the car based on speed and direction
        x = self.location[0] + self.speed * math.cos(self.direction)
        y = self.location[1] + self.speed * math.sin(self.direction)
        self.location = (x, y)
        logger.info(f"Updating car location to {self.location}")

    def __repr__(self):
        return f"Car(speed={self.speed}, direction={self.direction}, location={self.location})"
