# Robot-Coprocessors
A collection of component projects, source code and documentation for various on-board secondary robot coprocessors including vision tracking, distance sensors, LED lighting, and battery tagging/logging

## Components
* [Robot-Vision](Robot-Vision)
* Robot Controls
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
| Robot-Coprocessor-1 | `10.28.81.6` | 255.255.255.0 / 24 |
| Robot-Coprocessor-2 | `10.28.81.7` | 255.255.255.0 / 24 |

## Robot Vision

### Hardware 
* Board: [OrangePi 5 Pro - 16GB](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-5-Pro.html)
* Cameras (for AprilTag tracking) [Arducam OV9281 Global Shutter](https://www.arducam.com/product/arducam-120fps-global-shutter-usb-camera-board-1mp-720p-ov9281-uvc-webcam-module-with-low-distortion-m12-lens-without-microphones-for-computer-laptop-android-device-and-raspberry-pi/)
* Camera (for Object detection) [Arducam OV9782 Color Global Shutter](https://www.arducam.com/product/100fps-global-shutter-color-usb-camera-board-1mp-ov9782-uvc-webcam-module-with-low-distortion-m12-lens-without-microphones-for-computer-laptop-android-device-and-raspberry-pi-arducam/)

### Software
* Operating System + PhotonVision: [Orange Pi Installation](https://docs.photonvision.org/en/latest/docs/installation/sw_install/orange-pi.html) 
  * See [Robot-Vision](Robot-Vision) README for full setup and configuration details
* Configuration for SPI (lights) & I2C (sensors) interfaces for GPIO
  * Info: Device tree overlays: https://github.com/Joshua-Riek/ubuntu-rockchip/wiki/Ubuntu-24.04-LTS
  * Info: Orange Pi 5 Pro pin out: http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-5-Pro.html
  * `sudo nano /etc/default/u-boot`
  * `U_BOOT_FDT_OVERLAYS="device-tree/rockchip/overlay/rk3588-i2c5-m3.dtbo device-tree/rockchip/overlay/rk3588-spi4-m2-cs0-spidev.dtbo"`
  * sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 10
  * sudo apt-get install libgpiod2 python3-libgpiod
  * sudo apt-get install -y python3-smbus python3-dev i2c-tools
  * sudo adduser pi i2c
  * Inside venv as needed:
    * pip install gpiod
    * pip install adafruit-blinka
    * pip install adafruit-circuitpython-neopixel-spi

* Follow the setup and configuration steps for each of the controls coprocessor projects
  * [Robot-Sensors](Robot-Sensors)
  * [Robot-Lights](Robot-Lights)
  * [Robot-BatteryInfo](Robot-BatteryInfo)