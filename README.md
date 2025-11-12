# Robot-Coprocessors
A collection of component projects, source code and documentation for various on-board secondary robot coprocessors including vision tracking, distance sensors, LED lighting, and battery tagging/logging

## Components
* [Robot-Vision](Robot-Vision)
* [Robot-BatteryInfo](Robot-BatteryInfo)
* [Robot-Lights](Robot-Lights)

## Hardware & Software

### Base Hardware 
* Board: [OrangePi 5 Pro - 16GB](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-5-Pro.html)
* Cameras (for AprilTag tracking) [Arducam OV9281 Monochrome Global Shutter](https://www.arducam.com/product/arducam-120fps-global-shutter-usb-camera-board-1mp-720p-ov9281-uvc-webcam-module-with-low-distortion-m12-lens-without-microphones-for-computer-laptop-android-device-and-raspberry-pi/)
* Camera (for Object detection) [Arducam OV9782 Color Global Shutter](https://www.arducam.com/product/100fps-global-shutter-color-usb-camera-board-1mp-ov9782-uvc-webcam-module-with-low-distortion-m12-lens-without-microphones-for-computer-laptop-android-device-and-raspberry-pi-arducam/)

### Base Software
* Use base image for OrangePi 5 Pro from PhotonVision: [Quick Install](https://docs.photonvision.org/en/latest/docs/quick-start/quick-install.html) 
  * See [Robot-Vision](Robot-Vision) README for initial setup and networking, etc. configuration details for the base PhotonVision install
* Additional configuration for common SPI and I2C interfaces for GPIO (if applicable to the specific coprocessor instance)
  * OrangePi 5 Pro device tree modification: 
    * Device tree overlays: https://github.com/Joshua-Riek/ubuntu-rockchip/wiki/Ubuntu-24.04-LTS
      * `sudo nano /etc/default/u-boot`
      * Add line and save: `U_BOOT_FDT_OVERLAYS="device-tree/rockchip/overlay/rk3588-i2c5-m3.dtbo device-tree/rockchip/overlay/rk3588-spi4-m2-cs0-spidev.dtbo"`
      * `sudo u-boot-update`
    * Reference: Orange Pi 5 Pro GPIO pin out: http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-5-Pro.html
  * To enable internet access/routing on the base OrangePi 5 Pro image from PhotonVision:
    * `sudo sysctl -w net.ipv4.ping_group_range="0 65565"`
    * `sudo nmcli con mod static-enP4p65s0 ipv4.dns "8.8.8.8"`
  * Install Python 3.x: `sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 10`
  * Install additional global dependencies: `sudo apt install -y python-venv python3-dev python3-smbus libgpiod2 python3-libgpiod i2c-tools setuptools gcc swig pyscard libpcsclite-dev`
  * Elevate i2c access: `sudo adduser pi i2c`

* Follow the setup and configuration steps for each of the controls coprocessor projects
  * [Robot-BatteryInfo](Robot-BatteryInfo)
  * [Robot-Lights](Robot-Lights)
