# Robot-Lights (TO BE UPDATED)

## Capabilities
* Controller for WS2812B addressable LED strips and/or matrix panels to offload lighting operations from the roboRIO and robot code

## Hardware 
* [RPi GPIO Terminal Block HAT](https://www.amazon.com/dp/B08RDYDG6X)
* [BTF-Lighting WS2812B IC LED Strip](https://www.amazon.com/dp/B01CDTEEZ2)

## Software
* [Adafruit CircuitPython NeoPixel Library](https://docs.circuitpython.org/projects/neopixel/en/latest/)
* [Adafruit CircuitPython LED Animation Library](https://docs.circuitpython.org/projects/led-animation/en/latest/)

## Setup & Configuration
* Setup environment and install libraries (coproc must be connected to internet)
  * Run `cd Robot-Lights` to peform the setup and configuration within the project root
  * Following the steps outlined in this guide: [Automated Install - CircuitPython on RaspberryPi](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi)
    * Run `python -m venv env --system-site-packages`
    * Run `source env/bin/activate`
    * Run `pip install --upgrade pip`
    * Run `pip install --upgrade --extra-index-url=https://wpilib.jfrog.io/artifactory/api/pypi/wpilib-python-release-2024/simple pyntcore` (for NetworkTables Python lib via RobotPy)
    * Run `pip install --upgrade adafruit-python-shell`
    * Run `wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py`
    * Run `sudo -E env PATH=$PATH python3 raspi-blinka.py`
  * After completing the automated install steps and reconnecting, run `cd Robot-Lights` and `source env/bin/activate` for the Python virtual environment
  * Run `rm raspi-blinka.py`
  * Run `pip install --upgrade adafruit-circuitpython-neopixel`
  * Run `pip install --upgrade adafruit-circuitpython-led-animation`
  * Run `deactivate` to exit the Python virtual environment 
* Install and enable service to run main Python script at system boot
  * Run `sudo cp robot-lights.service /lib/systemd/system`
  * Run `sudo systemctl enable robot-lights`
  * Run `sudo systemctl start robot-lights`
  * Run `sudo reboot` 

## Development
* For local development on the coprocessor:
  * Connect remotely using terminal: `ssh pi@10.28.81.7`
  * Run `sudo systemctl stop robot-lights` (to stop the service and enable editing and testing)
  * Run `cd Robot-Lights`
  * Run `source env/bin/activate`
  * Run `nano main.py` (to edit/save the main Python script)
  * Run `sudo --preserve-env=PATH,VIRTUAL_ENV python -u main.py` to run the Python script outside the service context for development purposes
