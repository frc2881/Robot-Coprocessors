# Robot-Coprocessors
A collection of component projects, source code, and documentation for various on-board robot coprocessor functions including vision/localization (PhotonVision), sensors, lights, and battery tagging/logging

## Components
* [Robot-Vision](Robot-Vision)
* [Robot-BatteryInfo](Robot-BatteryInfo)
* [Robot-Lights](Robot-Lights)

## Hardware 
* See [Hardware & Electronics Invetory](https://github.com/frc2881/Documentation/wiki/Hardware-&-Electronics-Inventory#sensors)

## Software
* Use base image for OrangePi 5 Pro from PhotonVision: [Quick Install](https://docs.photonvision.org/en/latest/docs/quick-start/quick-install.html) 
  * See [Robot-Vision](Robot-Vision) README for initial setup and networking, etc. configuration details for the base PhotonVision install
* Additional configuration for common SPI interface for GPIO
  * OrangePi 5 Pro device tree modification: 
    * Device tree overlays: https://github.com/Joshua-Riek/ubuntu-rockchip/wiki/Ubuntu-24.04-LTS
      * `sudo nano /etc/default/u-boot`
      * Add line and save: `U_BOOT_FDT_OVERLAYS="device-tree/rockchip/overlay/rk3588-spi4-m2-cs0-spidev.dtbo"`
      * `sudo u-boot-update`
    * Reference: Orange Pi 5 Pro GPIO pin out: http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-5-Pro.html
  * To enable internet access/routing on the base OrangePi 5 Pro image from PhotonVision:
    * `sudo sysctl -w net.ipv4.ping_group_range="0 65565"`
    * `sudo nmcli con mod static-end1 ipv4.dns "8.8.8.8"`
  * Install Python 3.x: `sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 10`
  * Install additional global dependencies: `sudo apt install -y python-venv python3-dev python3-smbus libgpiod2 python3-libgpiod setuptools gcc swig pyscard libpcsclite-dev`

* Follow the setup and configuration steps for each of the controls coprocessor projects
  * [Robot-BatteryInfo](Robot-BatteryInfo)
  * [Robot-Lights](Robot-Lights)
  * [Robot-Vision](Robot-Vision)
