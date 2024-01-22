# Robot-Lights

## Capabilities
* Dedicated controller for WS2812B addressable LED strips and/or matrix panels to offload lighting operations from the roboRIO and robot code

## Hardware 
* Board: [Raspberry Pi Zero 2 W](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/)
* Networking: USB-C ethernet adapter + Micro-USB to USB-C adapter
* (TBD)
* Note: not covered here is power source conversion from robot 12V PDH to 5V/5A Micro-USB input or 5V/5A power source to the LED lights

## Software
* Operating System: [Raspberry Pi OS Lite (64-bit / bookworm)](https://www.raspberrypi.com/software/operating-systems/#raspberry-pi-os-64-bit)
* microSD card imaging: [Raspberry Pi Imager](https://www.raspberrypi.com/software/)

## Setup & Configuration
* Raspberry Pi Imager settings:
  * Enable ssh
  * Username: `pi`
  * Password: `ladycans`
  * Hostname: `frc2881-lights`
  * Time Zone: `Central (America/Chicago)`
  * Locale: `en-us`
* Raspberry Pi OS setup after initial boot:
  * Connect remotely using terminal: `ssh pi@10.28.81.???` (find the dynamic IP address assigned)
  * Run `sudo raspi-config`
    * Advanced options:
      * Expand filesystem
      * Enable network interface names
    * Exit / reboot / reconnect
  * Set the static IP address: `sudo nmcli con mod "Wired connection 1" ipv4.addresses 10.28.81.7/24 ipv4.gateway 10.28.81.1 ipv4.dns "10.28.81.1" ipv4.method manual`
  * Update and restart the connection: `sudo nmcli con up "Wired connection 1"`
* Base OS, Python, and library dependencies (RPi02W must be connected to internet)
  * Run `apt install -y git build-essential libc-dev`
  * Run `git clone https://github.com/frc2881/Robot-Coprocessors` (assuming you are in the `pi` home root)
  * Run `mv Robot-Coprocessors/Robot-Lights .` to relocate this project and code into the `pi` home root
  * Run `rm -rf Robot-Coprocessors` to remove everything else not needed on this coprocessor
  * Run `cd Robot-Lights` to peform the rest of the configuration within the project root
  * Follow the steps to update the Raspberry Pi OS and Python, set up the Python virtual environment (within `Robot-Lights`) and complete the [Automated Install](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi) steps to install the Adafruit Blinka library and tools
  * After completing the automated install steps and reconnecting, run `cd Robot-Lights` and `source env/bin/activate` for the Python virtual environment
  * Run `pip install python-decouple pyntcore` (for .env config access and the WPILib NetworkTables library)
  * ... more TBD ...

## (TBD)