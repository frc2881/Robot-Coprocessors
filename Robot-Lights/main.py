import atexit
import board
import time
import ntcore
import neopixel
from adafruit_led_animation import color, animation, helper
from adafruit_led_animation.animation import comet, chase, pulse

BOARD_PIN = board.D18
LIGHTS_COUNT = 29

nt = ntcore.NetworkTableInstance.getDefault()
nt.startClient4("coproc-robot-lights")
nt.setServer("10.28.81.2", ntcore.NetworkTableInstance.kDefaultPort4)

lightsModeTopic = nt.getStringTopic("/SmartDashboard/Robot/Lights/Mode").subscribe("Default")

colorHotPink = color.calculate_intensity((150, 0, 15), 1)
colorHotPinkDim = color.calculate_intensity((150, 0, 15), 0.1)

pixels = neopixel.NeoPixel(BOARD_PIN, LIGHTS_COUNT, brightness=1, auto_write=False, pixel_order=neopixel.GRB)

default = comet.Comet(pixels, speed=0.015, color=colorHotPink, tail_length=24)
visionNotReady = chase.Chase(pixels, speed=0.02, color=color.YELLOW, size=6, spacing=6)
intakeNotReady = chase.Chase(pixels, speed=0.02, color=color.BLUE, size=6, spacing=6)
intakeReady = chase.Chase(pixels, speed=0.02, color=color.GREEN, size=6, spacing=6, reverse=True)
launchReady = pulse.Pulse(pixels, speed=0.1, color=color.GREEN, period=0.2)

def onExit():
  pixels.fill(color.BLACK)
  pixels.show()

atexit.register(onExit)

while True:
 if nt.isConnected():
   match lightsModeTopic.get():
     case "VisionNotReady":
       visionNotReady.animate()
     case "IntakeNotReady":
       intakeNotReady.animate()
     case "IntakeReady":
       intakeReady.animate()
     case "LaunchReady":
       launchReady.animate()
     case "Default":
       default.animate()
     case _:
       pixels.fill(colorHotPinkDim)
       pixels.show()
 else:
  pixels.fill(colorHotPinkDim)
  pixels.show()
  time.sleep(1)