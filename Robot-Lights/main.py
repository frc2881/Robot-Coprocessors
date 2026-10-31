from enum import Enum, auto
import atexit
import time
import ntcore
from adafruit_extended_bus import ExtendedSPI as SPI
import neopixel_spi as neopixel
from adafruit_led_animation import color
from adafruit_led_animation.animation import chase, pulse, comet, solid, sparkle

class LightsMode(Enum):
  DEFAULT = auto()
  ROBOT_NOT_CONNECTED = auto()
  ROBOT_NOT_HOMED = auto()
  ROBOT_IS_HOMING = auto()
  VISION_NOT_READY = auto()
  HUB_STATE_ACTIVE = auto()
  HUB_STATE_ACTIVE_ENDING = auto()
  HUB_STATE_INACTIVE = auto()
  HUB_STATE_INACTIVE_ENDING = auto()
  ACTIVE_TARGET_NOT_IN_RANGE = auto()

LIGHTS_COUNT = 150
ANIMATION_SPEED = 0.01

COLOR_PINK = 0xCC000F

nt = ntcore.NetworkTableInstance.getDefault()
nt.startClient4("coproc-robot-lights")
nt.setServer("10.28.81.2", ntcore.NetworkTableInstance.kDefaultPort4)

lightsModeTopic = nt.getStringTopic("/Telemetry/Robot/Controllers/Lights/Mode").subscribe("Default")

spi = SPI(4, 0)

pixels = neopixel.NeoPixel_SPI(spi, LIGHTS_COUNT, brightness=1.0, auto_write=False, pixel_order=neopixel.GRB)

default = chase.Chase(pixels, speed=ANIMATION_SPEED, color=COLOR_PINK, size=10, spacing=25)
notConnected = sparkle.Sparkle(pixels, speed=ANIMATION_SPEED, color=COLOR_PINK, num_sparkles=5)
notHomed = pulse.Pulse(pixels, speed=ANIMATION_SPEED, color=color.RED, period=0.5, min_intensity=0.1, max_intensity=1.0)
isHoming = pulse.Pulse(pixels, speed=ANIMATION_SPEED, color=color.YELLOW, period=0.5, min_intensity=0.1, max_intensity=1.0)
noVision = pulse.Pulse(pixels, speed=ANIMATION_SPEED, color=color.BLUE, period=0.5, min_intensity=0.1, max_intensity=1.0)

hubStateActive = pulse.Pulse(pixels, speed=ANIMATION_SPEED, color=color.GREEN, period=0.5, min_intensity=0.33, max_intensity=1.0)
hubStateActiveEnding = chase.Chase(pixels, speed=ANIMATION_SPEED, color=color.GREEN, size=15, spacing=15)
hubStateInactive = pulse.Pulse(pixels, speed=ANIMATION_SPEED, color=color.CYAN, period=0.5, min_intensity=0.33, max_intensity=1.0)
hubStateInactiveEnding = chase.Chase(pixels, speed=ANIMATION_SPEED, color=color.CYAN, size=15, spacing=15)
activeTargetNotInRange = pulse.Pulse(pixels, speed=ANIMATION_SPEED, color=color.RED, period=0.15, min_intensity=0, max_intensity=1.0)

def onExit():
  pixels.fill(color.BLACK)
  pixels.show()

atexit.register(onExit)

while True:
  if nt.isConnected():
    match lightsModeTopic.get():
      case LightsMode.ROBOT_NOT_CONNECTED.name:
        notConnected.animate()
      case LightsMode.ROBOT_NOT_HOMED.name:
        notHomed.animate()
      case LightsMode.VISION_NOT_READY.name:
        noVision.animate()
      case LightsMode.ROBOT_IS_HOMING.name:
        isHoming.animate()
      case LightsMode.HUB_STATE_ACTIVE.name:
        hubStateActive.animate()
      case LightsMode.HUB_STATE_ACTIVE_ENDING.name:
        hubStateActiveEnding.animate()
      case LightsMode.HUB_STATE_INACTIVE.name:
        hubStateInactive.animate()
      case LightsMode.HUB_STATE_INACTIVE_ENDING.name:
        hubStateInactiveEnding.animate()
      case LightsMode.ACTIVE_TARGET_NOT_IN_RANGE.name:
        activeTargetNotInRange.animate()
      case _:
        default.animate()
  else:
      notConnected.animate()
