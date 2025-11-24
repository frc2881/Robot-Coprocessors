# Robot-BatteryInfo (TO BE UPDATED)

## Capabilities
* Python app for logging battery ID info from passive RFID-tagged batteries

## Hardware
* See [Hardware & Electronics Invetory](https://github.com/frc2881/Documentation/wiki/Hardware-&-Electronics-Inventory#sensors)

## Setup & Configuration
* Setup environment and install libraries (coproc must be connected to internet)
  * In the root foler `Robot-BatteryInfo`:
    * Run `python -m venv .venv --system-site-packages`
    * Run `source .venv/bin/activate`
    * Run `pip install --upgrade pip`
    * Run `pip install --upgrade --extra-index-url=https://wpilib.jfrog.io/artifactory/api/pypi/wpilib-python-release-2025/simple pyntcore` (for NetworkTables Python lib via RobotPy)
    * Run `pip install --upgrade setuptools`
    * Run `git clone https://github.com/LudovicRousseau/pyscard.git`
    * Run `cd pyscard`
    * Run `sudo ../env/bin/python setup.py build_ext install`
* Install and enable service to run main Python script at system boot
  * Run `sudo cp robot-batteryinfo.service /lib/systemd/system`
  * Run `sudo systemctl enable robot-batteryinfo`
  * Run `sudo systemctl start robot-batteryinfo`
  * Run `sudo reboot` 

## Operation
* Install NFC reader and tags for battery logging
  * Connect the NFC tag reader to coprocessor via USB
  * For each tag card applied to the selected batteries for tracking and logging usage data, use the native Android app [NFC Tools](https://play.google.com/store/apps/details?id=com.wakdev.wdnfc&gl=US) (or similar NFC tag reader/writer app) to write a single text data record to the tag in the format of `TEAM|ID|DATE` (ex: `2881|0001-A|2024-01`). 
  * Placement of the tag card on the battery must align close to the center point of the USB reader secured near the battery holder for the robot
