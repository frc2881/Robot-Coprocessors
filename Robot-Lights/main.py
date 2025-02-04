from enum import Enum, auto
import atexit
import board
import time
import ntcore
import neopixel_spi as neopixel
from adafruit_led_animation import color
from adafruit_led_animation.animation import comet, chase

class LightsMode(Enum):
  Default = auto()
  RobotNotReady = auto()
  VisionNotReady = auto()
  IntakeReady = auto()
  IntakeNotReady = auto()
  LaunchReady = auto()

LIGHTS_COUNT = 17

nt = ntcore.NetworkTableInstance.getDefault()
nt.startClient4("coproc-robot-lights")
nt.setServer("10.28.81.2", ntcore.NetworkTableInstance.kDefaultPort4)

lightsModeTopic = nt.getStringTopic("/SmartDashboard/Robot/Lights/Mode").subscribe("Default")

colorHotPink = color.calculate_intensity((150, 0, 15), 1)
colorHotPinkDim = color.calculate_intensity((150, 0, 15), 0.1)

pixels = neopixel.NeoPixel_SPI(board.SPI(), LIGHTS_COUNT, brightness=1, auto_write=False, pixel_order=neopixel.GRB)

default = comet.Comet(pixels, speed=0.02, color=colorHotPink, tail_length=15, bounce=True)
robotNotReady = chase.Chase(pixels, speed=0.02, color=color.RED, size=6, spacing=6)
visionNotReady = chase.Chase(pixels, speed=0.02, color=color.YELLOW, size=6, spacing=6)
intakeNotReady = chase.Chase(pixels, speed=0.02, color=color.BLUE, size=6, spacing=6)
intakeReady = chase.Chase(pixels, speed=0.02, color=color.GREEN, size=6, spacing=6, reverse=True)
launchReady = chase.Chase(pixels, speed=0.02, color=color.GREEN, size=18, spacing=2)

def onExit():
  pixels.fill(color.BLACK)
  pixels.show()

atexit.register(onExit)

while True:
 if nt.isConnected():
   match lightsModeTopic.get():
     case LightsMode.RobotNotReady.name:
       robotNotReady.animate()
     case LightsMode.VisionNotReady.name:
       visionNotReady.animate()
     case LightsMode.IntakeNotReady.name:
       intakeNotReady.animate()
     case LightsMode.IntakeReady.name:
       intakeReady.animate()
     case LightsMode.LaunchReady.name:
       launchReady.animate()
     case LightsMode.Default.name:
       default.animate()
     case _:
       pixels.fill(colorHotPinkDim)
       pixels.show()
 else:
  pixels.fill(colorHotPinkDim)
  pixels.show()
  time.sleep(1)