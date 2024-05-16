# Robot-BatteryInfo

## Capabilities
* Python app for logging battery ID info from passive RFID-tagged batteries

## Hardware
* Reader: [ACR122U NFC RFID 13.56MHz Contactless Smart Card Reader](https://www.amazon.com/dp/B07FCLY4S9)
* NFC Tag Cards: [THONSEN NTAG215 PVC Cards](https://www.amazon.com/dp/B087P24Q8K)

## Software
* Ensure the coprocessor is connected to the internet
* Connect remotely using terminal: `ssh pi@10.28.81.7`
* Run `git clone https://github.com/frc2881/Robot-Coprocessors` (assuming you are in the `pi` home root)
* Run `mv Robot-Coprocessors/Robot-BatteryInfo .` to relocate this project and code into the `pi` home root
* Run `rm -rf Robot-Coprocessors` to remove everything else not needed on this coprocessor
* Run `python -m venv env --system-site-packages`
* Run `source env/bin/activate`
* Run `pip install --upgrade --extra-index-url=https://wpilib.jfrog.io/artifactory/api/pypi/wpilib-python-release-2024/simple pyntcore` (for NetworkTables Python lib via RobotPy)
* Run `pip install --upgrade setuptools`
* Run `git clone https://github.com/LudovicRousseau/pyscard.git`
* Run `cd pyscard`
* Run `sudo ../env/bin/python setup.py build_ext install`
* Run `cd ..`
* Run `sudo cp robot-batteryinfo.service /lib/systemd/system`
* Run `sudo systemctl enable robot-batteryinfo`
* Run `sudo systemctl start robot-batteryinfo`
* Run `sudo reboot` 

## Operation
* Install NFC reader and tags for battery logging
  * Connect the NFC tag reader to coprocessor via USB
  * For each tag card applied to the selected batteries to track and log peformance data, use the native Android app [NFC Tools](https://play.google.com/store/apps/details?id=com.wakdev.wdnfc&gl=US) (or similar NFC tag reader/writer app) to write a single text data record to the tag in the format of `TEAM|ID|DATE` (ex: `2881|0001|2020-03`). 
  * Placement of the tag card on the battery must align close to the center point of the USB reader secured near the battery holder for the robot
