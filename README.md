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

## Robot Controls

### Hardware
* Board: [Raspberry Pi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)

### Software
* Operating System: [Raspberry Pi OS Lite (64-bit / bookworm)](https://www.raspberrypi.com/software/operating-systems/#raspberry-pi-os-64-bit)
* microSD card imaging: [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
* Python 3.12.x
