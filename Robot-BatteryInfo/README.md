# Robot-BatteryInfo

## Capabilities
* Dockerized python app for logging battery ID info from passive RFID-tagged batteries.

_Note: This hardware and software runs attached to the [Robot-Vision](Robot-Vision) coprocessor and environment_

## Hardware
* Reader: [ACR122U NFC RFID 13.56MHz Contactless Smart Card Reader](https://www.amazon.com/dp/B07FCLY4S9)
* NFC Tag Cards: [THONSEN NTAG215 PVC Cards](https://www.amazon.com/dp/B087P24Q8K)

## Software
* Ensure the coprocessor is connected to the internet
* Connect remotely using terminal: `ssh pi@10.28.81.6`
* Run `git clone https://github.com/frc2881/Robot-Coprocessors` (assuming you are in the `pi` home root)
* Run `mv Robot-Coprocessors/Robot-BatteryInfo .` to relocate this project and code into the `pi` home root
* Run `rm -rf Robot-Coprocessors` to remove everything else not needed on this coprocessor
* Run `cd Robot-BatteryInfo` to peform the rest of the configuration within the project root
* Run `sudo apt-get install docker.io docker-compose` (to install docker engine requirements if not already installed)
* Run `sudo usermod -aG docker pi` (to allow the pi user to run docker without using sudo)
* Close the ssh connection and reconnect / login
* Run `cd Robot-BatteryInfo` to peform the rest of the configuration within the project root
* Run `docker compose build` to build the docker image
* Run `docker compose up -d` to setup and run the image as a background daemon on system start
* The coprocessor can be disconnected from internet and is ready for local robot network operation

## Operation
* Install NFC reader and tags for battery logging
  * Connect the NFC tag reader to coprocessor via USB
  * For each tag card applied to the selected batteries to track and log peformance data, use the native Android app [NFC Tools](https://play.google.com/store/apps/details?id=com.wakdev.wdnfc&gl=US) (or similar NFC tag reader/writer app) to write a single text data record to the tag in the format of `TEAM|ID|DATE` (ex: `2881|0001|2020-03`). 
  * Placement of the tag card on the battery must align close to the center point of the USB reader secured near the battery holder for the robot


