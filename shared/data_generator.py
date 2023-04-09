import random


def generate_camera_data(length: int = 1):
    return [random.randint(1, 100) for _ in range(length)]


def generate_lidar_data(length: int = 1):
    # generate list of random length with random values of float type
    return [random.random() for _ in range(length)]


def generate_gps_data(length: int = 2):
    # generate latitude, longitude
    return tuple([random.random() * 100 for _ in range(length)])
