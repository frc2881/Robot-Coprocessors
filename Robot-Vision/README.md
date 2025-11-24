# Robot-Vision

## Capabilities
* AprilTag tracking for robot pose estimation 
* Object detection for game piece identification and relative position info

## Hardware & Software
* See readme at the root of [Robot-Coprocessors](https://github.com/frc2881/Robot-Coprocessors) 

## Setup & Configuration
* OrangePi 5 Pro OS image setup after initial boot:
  * Find the IP address on the network: `ping photonvision.local`
  * Connect remotely using terminal: `ssh pi@10.28.81.???`
  * Change the default password: `passwd` (change `raspberry` to  `ladycans`)
  * Open PhotonVision in web browser to confirm networking change and complete season-specific configuration and calibration: `http://10.28.81.???:5800`
* PhotonVision configuration (see [documentation](https://docs.photonvision.org/en/latest/index.html) for complete details):
  * Under Settings, configure NT server address (`10.28.81.2`), static IP address (`10.28.81.6` or `'.7`), host name (`frc2881-coproc-[1|2]`) and default network manager interface
  * Configure camera name, model, and run calibration with Charuco board for AprilTag tracking cameras (ask a mentor for help with Charuco board calibration process)
  * Select pipeline for each camera as appropriate (AprilTag or Object Detection)
  * For AprilTag pipeline, select highest resolution/FPS matching calibration (1280x720 @ 120FPS should be default, Decimate=2, Threads=3), 3D processing mode (ask a mentor for help with additional detailed calibration)
  * For Object Detection pipeline, select 1024x768 @ 30FPS/MJPEG
  * For all cameras, select the lowest possible stream resolution option for each camera (to minimize the bandwidth required for streaming back to the driver station app)
  * Generally follow all other recommended default settings from PhotonVision (enabling 3D mode for AprilTags, automatic exposure as default, etc.)
