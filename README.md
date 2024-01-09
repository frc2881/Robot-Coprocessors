# RobotCoprocessor
Robot coprocessor imaging, install, and configuration

## Hardware 
* [OrangePi 5 - 8GB](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-5-32GB.html)
* [Arducam 120fps Mono Global Shutter USB Camera](https://www.amazon.com/gp/product/B096M5DKY6)

## Software
#### Operating System: install and configure Armbian operating system, static IP networking, virtualization with docker, etc.
* TBD

## Subsystems
#### PhotonVision
* Clone this repo locally to the OrangePi and copy the PhotonVision folder into the user home directory
* Run `docker-compose build` (to build the PhotonVision image and container)
* Run `docker-compose up -d` (to start the PhotonVision container)

#### BatteryInfoLogger
* Follow the readme doc for cloning, building, and configuring the dockerized python app in this repo: [BatteryInfoLogger](https://github.com/frc2881/BatteryInfoLogger)
