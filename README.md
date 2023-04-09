# Self-Driving Car Project

This project implements a basic self-driving car using Python object-oriented programming concepts. The project has three main classes: `Vehicle`, `Sensor`, and `ControlComputer`. The `Vehicle` class represents the car, the `Sensor` class represents the sensors attached to the car, and the `ControlComputer` class represents the control computer that processes the sensor data and controls the car.

The `Vehicle` class has methods to control the car's speed, direction, and location. The `Sensor` class is an abstract base class that defines the basic functionality of all sensors. The `Camera`, `Lidar`, and `GPS` classes are derived from the `Sensor` class and implement specific sensor functionalities. The `ControlComputer` class connects to one or more sensors and a vehicle, processes data from the sensors, and controls the vehicle based on the processed sensor data.

## Classes

### Vehicle

The `Vehicle` class represents the car and has the following methods:

- `accelerate()`: Increases the speed of the car.
- `decelerate()`: Decreases the speed of the car.
- `steer(angle)`: Changes the direction of the car based on the given angle.
- `update_location()`: Updates the location of the car based on its current speed and direction.

### Sensor

The `Sensor` class is an abstract base class that defines the basic functionality of all sensors. It has the following methods:

- `collect_data()`: Collects data from the sensor.
- `process_data()`: Processes the collected data if necessary.
- `get_data()`: Returns the processed data.

### Camera

The `Camera` class is derived from the `Sensor` class and implements a camera sensor. It collects images and processes them to detect objects in the car's environment.

### Lidar

The `Lidar` class is derived from the `Sensor` class and implements a Lidar sensor. It collects distance measurements to objects in the car's environment.

### GPS

The `GPS` class is derived from the `Sensor` class and implements a GPS sensor. It collects the car's current location.

### ControlComputer

The `ControlComputer` class represents the control computer that processes sensor data and controls the car. It has the following methods:

- `connect_vehicle(vehicle)`: Connects the control computer to the car.
- `connect_sensor(sensor)`: Connects the control computer to a sensor.
- `process_data()`: Processes data from all connected sensors.
- `control_vehicle()`: Controls the connected vehicle based on processed sensor data.

## Usage

To use the self-driving car, first create instances of the `Vehicle`, `Camera`, `Lidar`, `GPS`, and `ControlComputer` classes. Then, connect the car and sensors to the control computer using the `connect_vehicle()` and `connect_sensor()` methods. Finally, process the sensor data using the `process_data()` method and control the car using the `control_vehicle()` method.

## Example
```python
from control_computer.control_computer import ControlComputer
from sensor.camera import Camera
from sensor.gps import GPS
from sensor.lidar import Lidar
from vehicle.car import Car

# Create instances of the Car, Camera, Lidar, GPS, and ControlComputer classes
car = Car()
camera = Camera()
lidar = Lidar()
gps = GPS()
computer = ControlComputer()

# Connect the car and sensors to the control computer
computer.connect_vehicle(car)
computer.connect_sensor(camera)
computer.connect_sensor(lidar)
computer.connect_sensor(gps)

# Collect and process data from all sensors
computer.process_data()

# Control the car based on the processed sensor data
computer.control_vehicle()
```

## Limitations

This implementation is a simplified example of a self-driving car and does not include many important features such as obstacle avoidance, traffic detection, and pedestrian detection. It is intended to demonstrate basic concepts of object-oriented programming and can be expanded upon to include more advanced features. Additionally, this implementation assumes that the car is driving on a flat, obstacle-free surface and does not account for uneven terrain or obstacles in the car's path.
