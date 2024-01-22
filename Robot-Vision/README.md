# Robot-Vision

## Capabilities
* AprilTag tracking for robot pose estimation 
* Object detection for game piece identification and relative position info

## Hardware 
* Board: [OrangePi 5 - 4GB](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-5.html)
* Cameras (for AprilTag tracking) [Arducam OV9281 Global Shutter](https://www.arducam.com/product/arducam-120fps-global-shutter-usb-camera-board-1mp-720p-ov9281-uvc-webcam-module-with-low-distortion-m12-lens-without-microphones-for-computer-laptop-android-device-and-raspberry-pi/)
* Camera (for Object detection) [ELP IMX179](https://www.elpcctv.com/elp-high-resolution-8-megapixel-sony-imx179-wide-angle-usb-camera-module-with-21mm-lens-p-239.html)

## Software
* Operating System + PhotonVision: [Orange Pi Installation](https://docs.photonvision.org/en/latest/docs/installation/sw_install/orange-pi.html)
* Arducam calibration import (1280x720): [calib_arducam_backward__0c45_6366__1280.json](./calib_arducam_backward__0c45_6366__1280.json)

## Setup & Configuration
* OrangePi 5 OS setup after initial boot:
  * Connect remotely using terminal: `ssh pi@10.28.81.???` (find the dynamic IP address assigned)
  * Change the default password: `passwd` (change `raspberry` to  `ladycans`)
  * Set the static IP address: `sudo nmcli con mod netplan-eth0 ipv4.addresses 10.28.81.6/24 ipv4.gateway 10.28.81.1 ipv4.dns "10.28.81.1" ipv4.method manual`
  * Update and restart the connection: `sudo nmcli con up netplan-eth0`
  * Open PhotonVision in web browser to confirm networking change and complete season-specific configuration and calibration: `http://10.28.81.6:5800`
* PhotonVision configuration (see [documentation](https://docs.photonvision.org/en/latest/index.html) for complete details):
  * Configure camera name, model, and import calibration file (for AprilTag tracking cameras)
  * Select pipeline for each camera as appropriate (AprilTag or Object Detection)
  * For AprilTag pipeline, select resolution of 1280x720 @ 120FPS/MJPEG (matching with imported calibration)
  * For Object Detection pipeline, select 1024x768 @ 30FPS/MJPEG
  * For all cameras, select the lowest possible stream resolution option for each camera (to minimize the bandwidth required for streaming back to the driver station app)
  * Generally follow all other recommended default settings from PhotonVision (enabling 3D mode for AprilTags, etc.)