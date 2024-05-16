# Robot-Coprocessors
A collection of component projects, source code and documentation for various on-board secondary robot coprocessors including vision tracking, distance sensors, LED lighting, and battery tagging/logging

## Components
* [Robot-Vision](Robot-Vision)
* Robot Controls
  * [Robot-Sensors](Robot-Sensors)
  * [Robot-Lights](Robot-Lights)
  * [Robot-BatteryInfo](Robot-BatteryInfo)

## Networking
Following the requirements from: [WPILib Docs - Networking - Static IP Configuration](https://docs.wpilib.org/en/stable/docs/networking/networking-introduction/ip-configurations.html#on-the-field-static-configuration)

| Component | IP Address | Subnet Mask |
|-----------|-----------|-----------|
| Radio | `10.28.81.1` | FMS |
| roboRIO | `10.28.81.2` | 255.255.255.0 |
| Driver Station | `10.28.81.5` | 255.0.0.0 / 8 |
| Robot-Vision | `10.28.81.6` | 255.255.255.0 / 24 |
| Robot-Controls | `10.28.81.7` | 255.255.255.0 / 24 |

## Robot Vision

### Hardware 
* Board: [OrangePi 5 Pro - 16GB](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-5-Pro.html)
* Cameras (for AprilTag tracking) [Arducam OV9281 Global Shutter](https://www.arducam.com/product/arducam-120fps-global-shutter-usb-camera-board-1mp-720p-ov9281-uvc-webcam-module-with-low-distortion-m12-lens-without-microphones-for-computer-laptop-android-device-and-raspberry-pi/)
* Camera (for Object detection) [Arducam OV9782 Color Global Shutter](https://www.arducam.com/product/100fps-global-shutter-color-usb-camera-board-1mp-ov9782-uvc-webcam-module-with-low-distortion-m12-lens-without-microphones-for-computer-laptop-android-device-and-raspberry-pi-arducam/)

### Software
* Operating System + PhotonVision: [Orange Pi Installation](https://docs.photonvision.org/en/latest/docs/installation/sw_install/orange-pi.html)
* Arducam calibration import 
  * OV9281 @ 1280x720: [calib_arducam_backward__0c45_6366__1280.json](./calib_arducam_backward__0c45_6366__1280.json)
  * OV9782 @ 1280x720: [calib_3937__0c45_6366__1280.json](./calib_3937__0c45_6366__1280.json)

See: [Robot-Vision](Robot-Vision) README for full setup and configuration details

## Robot Controls

### Hardware
* Board: [Raspberry Pi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)
* See each controls project README for additional hardware components

### Software
* Operating System: [Raspberry Pi OS Lite (64-bit / bookworm)](https://www.raspberrypi.com/software/operating-systems/#raspberry-pi-os-64-bit)
* microSD card imaging: [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
* Python 3.11.x
* See each controls project README for additional software components

## Setup & Configuration
* Raspberry Pi Imager settings:
  * General
    * Set hostname: `frc2881-controls`.local
    * Set username and password: `pi` / `ladycans`
    * No WLAN
    * Set locale settings: `Central (America/Chicago)` / `us`
  * Services
    * Enable SSH: Use password authentication 
* Raspberry Pi OS setup after initial boot:
  * Connect remotely using terminal: `ssh pi@10.28.81.???` (find the dynamic IP address assigned using Angry IP Scanner looking for port 22)
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
* Base OS and Python updates, library installs and project cloning (RPi must be connected to the internet)
  * Connect remotely using terminal: `ssh pi@10.28.81.7` 
  * Run `sudo apt-get update`
  * Run `sudo apt-get upgrade` 
  * Run `sudo apt-get install -y git build-essential libc-dev`
  * Run `sudo apt-get install -y --upgrade python3-pip python3-setuptools python3.11-venv`
  * Run `git clone https://github.com/frc2881/Robot-Coprocessors` (assuming you are in the `pi` home root)
  * Run `mv Robot-Coprocessors/* .` to relocate all projects and code into the `pi` home root
  * Run `rm -rf Robot-Coprocessors` to remove the empty repo folder
* Follow the setup and configuration steps for each of the controls coprocessor projects
  * [Robot-Sensors](Robot-Sensors)
  * [Robot-Lights](Robot-Lights)
  * [Robot-BatteryInfo](Robot-BatteryInfo)