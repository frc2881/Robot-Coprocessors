# Robot-Sensors (TO BE UPDATED)

## Capabilities
* Fine-grained distance measurement using ToF (Time of Flight) sensors for object proximity detection internally within the robot mechanisms and/or externally around the robot chassis as appropriate

## Hardware 
* [Adafruit Distance Sensor - VL53L4CD (Qwiic)](https://www.adafruit.com/product/5396) (1+)
* [SparkFun QwiicBus - EndPoint](https://www.sparkfun.com/products/16988) (2 per sensor)
* [Flexible Qwiic Cable - 50mm](https://www.sparkfun.com/products/17260) (2 + 2 per sensor)
* [Adafruit I2C Active Terminator - LTC4311 (Qwiic)](https://www.adafruit.com/product/4756) (1)
* [Adafruit I2C Multiplexer - PCA9548 (Qwiic)](https://www.adafruit.com/product/5626) (1)

## Software
* [Adafruit CircuitPython VL53L4CD Library](https://docs.circuitpython.org/projects/vl53l4cd/en/latest/)
* [Adafruit CircuitPython TCA9548A Library](https://docs.circuitpython.org/projects/tca9548a/en/latest/)

## Setup & Configuration
* Setup environment and install libraries (coproc must be connected to internet)
  * In the root foler `Robot-Sensors`:
    * Run `python -m venv .venv --system-site-packages`
    * Run `source .venv/bin/activate`
    * Run `pip install --upgrade pip`
    * Run `pip install --upgrade --extra-index-url=https://wpilib.jfrog.io/artifactory/api/pypi/wpilib-python-release-2025/simple pyntcore` (for NetworkTables Python lib via RobotPy)
    * Run `pip install --upgrade gpiod adafruit-python-shell adafruit-blinka adafruit-circuitpython-tca9548a adafruit-circuitpython-vl53l4cd`
* Install and enable service to run main Python script at system boot
  * Run `sudo cp robot-sensors.service /lib/systemd/system`
  * Run `sudo systemctl enable robot-sensors`
  * Run `sudo systemctl start robot-sensors`
  * Run `sudo reboot` 

## Development
* For local development on the coprocessor:
  * Connect remotely using terminal: `ssh pi@10.28.81.7`
  * Run `sudo systemctl stop robot-sensors` (to stop the service and enable editing and testing)
  * Run `cd Robot-Sensors`
  * Run `source .venv/bin/activate`
  * Run `nano main.py` (to edit/save the main Python script)
  * Run `sudo --preserve-env=PATH,VIRTUAL_ENV python -u main.py` to run the Python script outside the service context for development purposes

