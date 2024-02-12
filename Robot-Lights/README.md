# Robot-Lights

## Capabilities
* Dedicated controller for WS2812B addressable LED strips and/or matrix panels to offload lighting operations from the roboRIO and robot code

## Hardware 
* Board: [Raspberry Pi Zero 2 W](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/)
* Networking: USB-C ethernet adapter + Micro-USB to USB-C adapter
* [RPi Pinout Terminal Block Breakout Board](https://www.amazon.com/dp/B08LH9ZBQ1)
* (TBD)
* Note: not covered here is power source conversion from robot 12V PDH to 5V/5A Micro-USB input or 5V/5A power source to the LED lights

## Software
* Operating System: [Raspberry Pi OS Lite (64-bit / bookworm)](https://www.raspberrypi.com/software/operating-systems/#raspberry-pi-os-64-bit)
* microSD card imaging: [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
* [Adafruit CircuitPython LED Animation Library](https://docs.circuitpython.org/projects/led-animation)

## Setup & Configuration
* Raspberry Pi Imager settings:
  * General
    * Set hostname: `frc2881-lights`.local
    * Set username and password: `pi` / `ladycans`
    * No WLAN
    * Set locale settings: `Central (America/Chicago)` / `us`
  * Services
    * Enable SSH: Use password authentication 
* Raspberry Pi OS setup after initial boot:
  * Connect remotely using terminal: `ssh pi@10.28.81.???` (find the dynamic IP address assigned)
  * Run `sudo raspi-config`
    * Interface Options:
      * Enabled I2C and SPI interfaces
    * Localization Options:
      * Locale: disable en_GB / enable: en_US / select en_US.UTF-8
    * Advanced options:
      * Expand filesystem
      * Enable (predictable) network interface names
    * Exit / reboot / reconnect
  * Set the static IP address: `sudo nmcli con mod "Wired connection 1" ipv4.addresses 10.28.81.8/24 ipv4.gateway 10.28.81.1 ipv4.dns "10.28.81.1" ipv4.method manual`
  * Update and restart the connection: `sudo nmcli con up "Wired connection 1"`
* Base OS, Python, and library dependencies (RPi02W must be connected to internet)
  * Connect remotely using terminal: `ssh pi@10.28.81.8` 
  * Run `sudo apt-get update`
  * Run `sudo apt-get upgrade` 
  * Run `sudo apt-get install -y git build-essential libc-dev`
  * Run `git clone https://github.com/frc2881/Robot-Coprocessors` (assuming you are in the `pi` home root)
  * Run `mv Robot-Coprocessors/Robot-Lights .` to relocate this project and code into the `pi` home root
  * Run `rm -rf Robot-Coprocessors` to remove everything else not needed on this coprocessor
  * Run `cd Robot-Lights` to peform the rest of the configuration within the project root
  * Following the steps outlined in this guide: [Automated Install](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi)
    * Run `sudo apt-get install python3-pip`
    * Run `sudo apt install --upgrade python3-setuptools`
    * Run `sudo apt install python3.11-venv`
    * Run `python -m venv env --system-site-packages`
    * Run `source /home/pi/Robot-Lights/env/bin/activate`
    * Run `pip install --upgrade python-decouple` (for .env config access)
    * Run `pip install --upgrade --extra-index-url=https://wpilib.jfrog.io/artifactory/api/pypi/wpilib-python-release-2024/simple pyntcore` (for NetworkTables Python lib via RobotPy)
    * Run `pip install --upgrade adafruit-python-shell`
    * Run `wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py`
    * Run `sudo -E env PATH=$PATH python3 raspi-blinka.py`
  * After completing the automated install steps and reconnecting, run `cd Robot-Lights` and `source /home/pi/Robot-Lights/env/bin/activate` for the Python virtual environment
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
  * Connect remotely using terminal: `ssh pi@10.28.81.8`
  * Run `sudo systemctl stop robot-lights` (to stop the service and enable editing and testing)
  * Run `cd Robot-Lights`
  * Run `source /home/pi/Robot-Lights/env/bin/activate`
  * Run `nano main.py` (to edit/save the main Python script)
  * Run `sudo --preserve-env=PATH,VIRTUAL_ENV python -u main.py` to run the Python script outside the service context for development purposes
* For remote development on the coprocessor using VSCode 
  * Install the `Remote - SSH` extension from Microsoft and follow the instructions for connecting to a remote host and opening a local folder (`Robot-Sensors`)
  * Using the integrated terminal, using the same commands for local development to stop the service and activate the Python virtual environment
  * Use the Explorer to access and edit the remote files as needed for development and testing