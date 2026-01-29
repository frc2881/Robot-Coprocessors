# Robot-Vision

## Capabilities
* AprilTag tracking for robot pose estimation 
* Object detection for game piece identification and relative position info

## Hardware 
* See [Hardware & Electronics Invetory](https://github.com/frc2881/Documentation/wiki/Hardware-&-Electronics-Inventory#sensors)

## Software
* See [Robot-Coprocessors](https://github.com/frc2881/Robot-Coprocessors) 

## Setup & Configuration
* OrangePi 5 Pro OS image setup after initial boot:
  * Find the IP address on the network: `ping photonvision.local`
  * Connect remotely using terminal: `ssh pi@10.28.81.???` (pw: raspberry)
  * Change the default password: `passwd` (change `raspberry` to  `ladycans`)
  * Open PhotonVision in web browser to confirm networking change and complete season-specific configuration and calibration: `http://10.28.81.???:5800`
* PhotonVision configuration (see [documentation](https://docs.photonvision.org/en/latest/index.html) for complete details):
  * Under Settings, configure NT server address (`10.28.81.2`), static IP address (`10.28.81.6` or `'.7`), host name (`frc2881-coproc-[1|2]`) and default network manager interface
  * Generally follow all other recommended default settings from PhotonVision documentation (enabling 3D mode for AprilTags, exposure, etc.). Season-specific configuration will be captured in build notes for that robot.
  * Note: for all cameras, select the lowest possible stream output resolution option in order to minimize the bandwidth required for streaming back to the driver station app
  
