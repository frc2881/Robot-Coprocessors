import atexit
import board
import time
import ntcore
import neopixel
from adafruit_led_animation import color, animation, helper
from adafruit_led_animation.animation import sparklepulse

BOARD_PIN = board.D18
LIGHTS_COUNT = 150

nt = ntcore.NetworkTableInstance.getDefault()
nt.startClient4("coproc-robot-lights")
nt.setServer("10.28.81.2", ntcore.NetworkTableInstance.kDefaultPort4)

lightsModeTopic = nt.getStringTopic("/SmartDashboard/Robot/Lights/Mode").subscribe("DEFAULT")
lightsMode = "DEFAULT"

colorHotPink = color.calculate_intensity((150, 0, 10), 1)

pixels = neopixel.NeoPixel(BOARD_PIN, LIGHTS_COUNT, brightness=1, auto_write=False, pixel_order=neopixel.GRB)

sparklePulse = sparklepulse.SparklePulse(pixels, speed=0.05, period=3, color=colorHotPink)

def onExit():
  pixels.fill(color.BLACK)
  pixels.show()

atexit.register(onExit)

while True:
  if nt.isConnected():
    lightsMode = lightsModeTopic.get()
    match lightsMode:
      case "DEFAULT":
        sparklePulse.animate()
      case _:
        pixels.fill(color.BLACK)
        pixels.show()
        time.sleep(0.02)
  else:
    time.sleep(1)