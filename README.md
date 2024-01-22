# Robot-Coprocessors
A collection of component projects, source code and documentation for various on-board secondary robot coprocessors including vision tracking, distance sensors, LED lighting, and battery tagging/logging

## Components
* [Robot-Vision](Robot-Vision)
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
| Robot-Sensors | `10.28.81.7` | 255.255.255.0 / 24 |
| Robot-Lights | `10.28.81.8` | 255.255.255.0 / 24 |

## (TBD)