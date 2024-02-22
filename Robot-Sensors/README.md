# Robot-Sensors 

## Capabilities
* Fine-grained distance measurement using ToF (Time of Flight) sensors for object proximity detection internally within the robot mechanisms and/or externally around the robot chassis as appropriate

## Hardware 
* Board: [Raspberry Pi Zero 2 W](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/)
* Networking: USB-C ethernet adapter + Micro-USB to USB-C adapter
* [SparkFun Qwiic pHat](https://www.sparkfun.com/products/15945) (1)
* [SparkFun Qwiic Mux Breakout - 8 Channel (TCA9548A)](https://www.sparkfun.com/products/16784) (1)
* [SparkFun Distance Sensor - 1.3 Meter, VL53L4CD (Qwiic)](https://www.sparkfun.com/products/18993) (1+)
* [SparkFun QwiicBus - EndPoint](https://www.sparkfun.com/products/16988) (2 per sensor)
* [Flexible Qwiic Cable - 50mm](https://www.sparkfun.com/products/17260) (2 + 2 per sensor)
* Note: not covered here is power source conversion from robot 12V PDH to 5V/5A Micro-USB input

## Software
* Operating System: [Raspberry Pi OS Lite (64-bit / bookworm)](https://www.raspberrypi.com/software/operating-systems/#raspberry-pi-os-64-bit)
* microSD card imaging: [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
* [Adafruit CircuitPython VL53L4CD Library](https://docs.circuitpython.org/projects/vl53l4cd/en/latest/)

## Setup & Configuration
* Raspberry Pi Imager settings:
  * General
    * Set hostname: `frc2881-sensors`.local
    * Set username and password: `pi` / `ladycans`
    * No WLAN
    * Set locale settings: `Central (America/Chicago)` / `us`
  * Services
    * Enable SSH: Use password authentication 
* Raspberry Pi OS setup after initial boot:
  * Connect remotely using terminal: `ssh pi@10.28.81.???` (find the dynamic IP address assigned)
  * Run `sudo raspi-config`
    * Interface Options:
      * Enable I2C and SPI interfaces
    * Localization Options:
      * Locale: disable en_GB / enable: en_US / select en_US.UTF-8
    * Advanced options:
      * Expand filesystem
      * Enable (predictable) network interface names
    * Exit / reboot / reconnect
  * Set the static IP address: `sudo nmcli con mod "Wired connection 1" ipv4.addresses 10.28.81.7/24 ipv4.gateway 10.28.81.1 ipv4.dns "10.28.81.1" ipv4.method manual`
  * Update and restart the connection: `sudo nmcli con up "Wired connection 1"`
* Base OS, Python, and library dependencies (RPi02W must be connected to internet)
  * Connect remotely using terminal: `ssh pi@10.28.81.7` 
  * Run `sudo apt-get update`
  * Run `sudo apt-get upgrade` 
  * Run `sudo apt-get install -y git build-essential libc-dev`
  * Run `git clone https://github.com/frc2881/Robot-Coprocessors` (assuming you are in the `pi` home root)
  * Run `mv Robot-Coprocessors/Robot-Sensors .` to relocate this project and code into the `pi` home root
  * Run `rm -rf Robot-Coprocessors` to remove everything else not needed on this coprocessor
  * Run `cd Robot-Sensors` to peform the rest of the configuration within the project root
  * Following the steps outlined in this guide: [Automated Install](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi)
    * Run `sudo apt-get install python3-pip`
    * Run `sudo apt install --upgrade python3-setuptools`
    * Run `sudo apt install python3.11-venv`
    * Run `python -m venv env --system-site-packages`
    * Run `source /home/pi/Robot-Sensors/env/bin/activate`
    * Run `pip install --upgrade --extra-index-url=https://wpilib.jfrog.io/artifactory/api/pypi/wpilib-python-release-2024/simple pyntcore` (for NetworkTables Python lib via RobotPy)
    * Run `pip install --upgrade adafruit-python-shell`
    * Run `wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py`
    * Run `sudo -E env PATH=$PATH python3 raspi-blinka.py`
  * After completing the automated install steps and reconnecting, run `cd Robot-Sensors` and `source /home/pi/Robot-Sensors/env/bin/activate` for the Python virtual environment
  * Run `rm raspi-blinka.py`
  * Run `pip install --upgrade adafruit-circuitpython-tca9548a` (for TCA9548A I2C multiplexer)
  * Run `pip install --upgrade adafruit-circuitpython-vl53l4cd` (for VL53L4CD ToF distance sensor)
  * Run `pip install --upgrade adafruit-circuitpython-vl53l0x` (for VL53L0X ToF distance sensor)
  * Run `deactivate` to exit the Python virtual environment 
* Set the I2C clock speed to 100 kHz for the RPi02W
  * Run `sudo nano /boot/config.txt`
  * Add the line `dtparam=i2c_arm_baudrate=100000`
  * Save the file and exit nano
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
  * Run `source /home/pi/Robot-Sensors/env/bin/activate`
  * Run `nano main.py` (to edit/save the main Python script)
  * Run `python -u main.py` to run the Python script outside the service context for development purposes
* For remote development on the coprocessor using VSCode 
  * Install the `Remote - SSH` extension from Microsoft and follow the instructions for connecting to a remote host and opening a local folder (`Robot-Sensors`)
  * Using the integrated terminal, using the same commands for local development to stop the service and activate the Python virtual environment
  * Use the Explorer to access and edit the remote files as needed for development and testing
