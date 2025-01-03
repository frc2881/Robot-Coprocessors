# Robot-Vision

## Capabilities
* AprilTag tracking for robot pose estimation 
* Object detection for game piece identification and relative position info

## Hardware 
* Board: [OrangePi 5 Pro - 16GB](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-5-Pro.html)
* Cameras (for AprilTag tracking) [Arducam OV9281 Global Shutter](https://www.arducam.com/product/arducam-120fps-global-shutter-usb-camera-board-1mp-720p-ov9281-uvc-webcam-module-with-low-distortion-m12-lens-without-microphones-for-computer-laptop-android-device-and-raspberry-pi/)
* Camera (for Object detection) [Arducam OV9782 Color Global Shutter](https://www.arducam.com/product/100fps-global-shutter-color-usb-camera-board-1mp-ov9782-uvc-webcam-module-with-low-distortion-m12-lens-without-microphones-for-computer-laptop-android-device-and-raspberry-pi-arducam/)

## Software
* Operating System + PhotonVision: [Orange Pi Installation](https://docs.photonvision.org/en/latest/docs/installation/sw_install/orange-pi.html)
* Arducam serial number utility

## Setup & Configuration
* OrangePi 5 OS setup after initial boot:
  * Find the IP address on the network: `ping photonvision.local`
  * Connect remotely using terminal: `ssh pi@10.28.81.???`
  * Change the default password: `passwd` (change `raspberry` to  `ladycans`)
  * Open PhotonVision in web browser to confirm networking change and complete season-specific configuration and calibration: `http://10.28.81.???:5800`
* PhotonVision configuration (see [documentation](https://docs.photonvision.org/en/latest/index.html) for complete details):
  * Under Settings, configure NT server address (`10.28.81.2`), static IP address (`10.28.81.6`), host name (`frc2881-coproc-[1|2]`) and network manager interface
  * Configure camera name, model, and run calibration with Charuco board for AprilTag tracking cameras (ask a mentor for help with Charuco board calibration process)
  * Select pipeline for each camera as appropriate (AprilTag or Object Detection)
  * For AprilTag pipeline, select resolution matching with imported calibration
  * For Object Detection pipeline, select 1024x768 @ 30FPS/MJPEG
  * For all cameras, select the lowest possible stream resolution option for each camera (to minimize the bandwidth required for streaming back to the driver station app)
  * Generally follow all other recommended default settings from PhotonVision (enabling 3D mode for AprilTags, etc.)