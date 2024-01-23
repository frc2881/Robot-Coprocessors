# Robot-Sensors 

## Capabilities
* Fine-grained distance measurement using ToF (Time of Flight) sensors for object proximity detection internally within the robot mechanisms and/or externally around the robot chassis as appropriate

## Hardware 
* Board: [Raspberry Pi Zero 2 W](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/)
* Networking: USB-C ethernet adapter + Micro-USB to USB-C adapter
* [SparkFun Qwiic SHIM for Raspberry Pi](https://www.sparkfun.com/products/15794) (1)
* [SparkFun Qwiic Mux Breakout - 8 Channel (TCA9548A)](https://www.sparkfun.com/products/16784) (1)
* [SparkFun Distance Sensor - 1.3 Meter, VL53L4CD (Qwiic)](https://www.sparkfun.com/products/18993) (1+)
* [SparkFun QwiicBus - EndPoint](https://www.sparkfun.com/products/16988) (2 per sensor)
* [Flexible Qwiic Cable - 50mm](https://www.sparkfun.com/products/17260) (2 + 2 per sensor)
* Note: not covered here is power source conversion from robot 12V PDH to 5V/5A Micro-USB input

## Software
* Operating System: [Raspberry Pi OS Lite (64-bit / bookworm)](https://www.raspberrypi.com/software/operating-systems/#raspberry-pi-os-64-bit)
* microSD card imaging: [Raspberry Pi Imager](https://www.raspberrypi.com/software/)

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
      * Enabled I2C and SPI interfaces
    * Localization Options:
      * Locale: disable en_GB / enable: en_US / select en_US.UTF-8
    * Advanced options:
      * Expand filesystem
      * Enable (predictable) network interface names
    * Exit / reboot / reconnect
  * Set the static IP address: `sudo nmcli con mod "Wired connection 1" ipv4.addresses 10.28.81.7/24 ipv4.gateway 10.28.81.1 ipv4.dns "10.28.81.1" ipv4.method manual`
  * Update and restart the connection: `sudo nmcli con up "Wired connection 1"`
* Base OS, Python, and library dependencies (RPi02W must be connected to internet)
  * Run `sudo apt-get update`
  * Run `sudo apt-get upgrade` 
  * Run `sudo apt-get install -y git build-essential libc-dev`
  * Run `git clone https://github.com/frc2881/Robot-Coprocessors` (assuming you are in the `pi` home root)
  * Run `mv Robot-Coprocessors/Robot-Sensors .` to relocate this project and code into the `pi` home root
  * Run `rm -rf Robot-Coprocessors` to remove everything else not needed on this coprocessor
  * Run `cd Robot-Sensors` to peform the rest of the configuration within the project root
  * Follow the steps to update the Raspberry Pi OS and Python, set up the Python virtual environment (within `Robot-Sensors`) and complete the [Automated Install](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi) steps to install the Adafruit Blinka library and tools
  * After completing the automated install steps and reconnecting, run `cd Robot-Sensors` and `source env/bin/activate` for the Python virtual environment
  * Run `pip install python-decouple pyntcore` (for .env config access and the WPILib NetworkTables library)
  * Run `pip install adafruit-circuitpython-tca9548a` (for the I2C multiplexer)
  * Run `pip install adafruit-circuitpython-vl53l4cd` (for the Tof distance sensor)
  * ... more TBD ...

## (TBD)
