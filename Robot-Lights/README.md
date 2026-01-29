# Robot-Lights (TO BE UPDATED)

## Capabilities
* Controller for WS2812B addressable LED strips and/or matrix panels to offload lighting operations from the roboRIO and robot code

## Hardware 
* See [Hardware & Electronics Invetory](https://github.com/frc2881/Documentation/wiki/Hardware-&-Electronics-Inventory#sensors)

## Software
* [Adafruit CircuitPython NeoPixel Library](https://docs.circuitpython.org/projects/neopixel/en/latest/)
* [Adafruit CircuitPython LED Animation Library](https://docs.circuitpython.org/projects/led-animation/en/latest/)

## Setup & Configuration
* Setup environment and install libraries (coproc must be connected to internet)
  * In the root foler `Robot-Lights`:
    * Run `python -m venv .venv --system-site-packages`
    * Run `source .venv/bin/activate`
    * Run `pip install --upgrade pip`
    * Run `pip install --upgrade --extra-index-url=https://wpilib.jfrog.io/artifactory/api/pypi/wpilib-python-release-2026/simple pyntcore` (for NetworkTables Python lib via RobotPy)
    * Run `pip install --upgrade gpiod adafruit-python-shell adafruit-blinka adafruit-circuitpython-neopixel-spi adafruit-circuitpython-led-animation`
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
  * Run `source .venv/bin/activate`
  * Run `nano main.py` (to edit/save the main Python script)
  * Run `sudo --preserve-env=PATH,VIRTUAL_ENV python -u main.py` to run the Python script outside the service context for development purposes
