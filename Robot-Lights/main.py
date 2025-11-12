from enum import Enum, auto
import atexit
import board
import time
import ntcore
import neopixel_spi as neopixel
from adafruit_led_animation import color
from adafruit_led_animation.animation import chase, pulse, solid

class LightsMode(Enum):
  Default = auto()
  RobotNotConnected = auto()
  RobotNotHomed = auto()
  VisionNotReady = auto()

LIGHTS_COUNT = 128
ANIMATION_SPEED = 0.03

nt = ntcore.NetworkTableInstance.getDefault()
nt.startClient4("coproc-robot-lights")
nt.setServer("10.28.81.2", ntcore.NetworkTableInstance.kDefaultPort4)

lightsModeTopic = nt.getStringTopic("/SmartDashboard/Robot/Lights/Mode").subscribe("Default")

pixels = neopixel.NeoPixel_SPI(board.SPI(), LIGHTS_COUNT, brightness=0.2, auto_write=False, pixel_order=neopixel.GRB)

default = chase.Chase(pixels, speed=ANIMATION_SPEED, color=0x99000A, size=6, spacing=3)
error = pulse.Pulse(pixels, speed=ANIMATION_SPEED, color=color.RED, period=2.0, min_intensity=0, max_intensity=0.25)
warning = pulse.Pulse(pixels, speed=ANIMATION_SPEED, color=color.AMBER, period=1.5, min_intensity=0.01, max_intensity=0.5)

alignedToPosition = chase.Chase(pixels, speed=ANIMATION_SPEED, color=color.GREEN, size=4, spacing=2)

def onExit():
  pixels.fill(color.BLACK)
  pixels.show()

atexit.register(onExit)

while True:
  if nt.isConnected():
    match lightsModeTopic.get():
      case LightsMode.RobotNotConnected.name:
        error.animate()
      case LightsMode.RobotNotHomed.name:
        warning.animate()
      case LightsMode.VisionNotReady.name:
        warning.animate()
      case _:
        default.animate()
  else:
    error.animate()
