# Robot-Sensors 

## Capabilities
* Fine-grained distance measurement using ToF (Time of Flight) sensors for object proximity detection internally within the robot mechanisms and/or externally around the robot chassis as appropriate

## Hardware 
* [Adafruit Distance Sensor - VL53L4CD (Qwiic)](https://www.adafruit.com/product/5396) (1+)
* [Adafruit Hot-Swap I2C Buffer - TCA4307 (Qwiic)](https://www.adafruit.com/product/5159) (1)
* [Adafruit I2C Multiplexer - PCA9548 (Qwiic)](https://www.adafruit.com/product/5626) (1)
* [SparkFun I2C SHIM (Qwiic)](https://www.sparkfun.com/products/15794) (1)
* [SparkFun QwiicBus - EndPoint](https://www.sparkfun.com/products/16988) (2 per sensor)
* [Flexible Qwiic Cable - 50mm](https://www.sparkfun.com/products/17260) (2 + 2 per sensor)

## Software
* [Adafruit CircuitPython VL53L4CD Library](https://docs.circuitpython.org/projects/vl53l4cd/en/latest/)
* [Adafruit CircuitPython TCA9548A Library](https://docs.circuitpython.org/projects/tca9548a/en/latest/)

## Setup & Configuration
* Setup environment and install libraries (RPi must be connected to internet)
  * Run `sudo nano /boot/firmware/config.txt`
    * Add the following line `dtparam=i2c_arm_baudrate=100000` right after the existing dtparam entries
    * Save the file and reboot the pickup the clock speed change
  * Run `cd Robot-Sensors` to peform the setup and configuration within the project root
  * Following the steps outlined in this guide: [Automated Install - CircuitPython on RaspberryPi](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi)
    * Run `python -m venv env --system-site-packages`
    * Run `source env/bin/activate`
    * Run `pip install --upgrade pip`
    * Run `pip install --upgrade --extra-index-url=https://wpilib.jfrog.io/artifactory/api/pypi/wpilib-python-release-2024/simple pyntcore` (for NetworkTables Python lib via RobotPy)
    * Run `pip install --upgrade adafruit-python-shell`
    * Run `wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py`
    * Run `sudo -E env PATH=$PATH python3 raspi-blinka.py`
  * After completing the automated install steps and reconnecting, run `cd Robot-Sensors` and `source env/bin/activate` for the Python virtual environment
  * Run `rm raspi-blinka.py`
  * Run `pip install --upgrade adafruit-circuitpython-tca9548a` (for TCA9548A I2C multiplexer)
  * Run `pip install --upgrade adafruit-circuitpython-vl53l4cd` (for VL53L4CD ToF distance sensor)
  * Run `deactivate` to exit the Python virtual environment 
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
  * Run `source env/bin/activate`
  * Run `nano main.py` (to edit/save the main Python script)
  * Run `sudo --preserve-env=PATH,VIRTUAL_ENV python -u main.py` to run the Python script outside the service context for development purposes

