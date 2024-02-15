from decouple import config
import atexit
import time
import ntcore
import board
import neopixel
from adafruit_led_animation import color, animation, helper
from adafruit_led_animation.animation import sparklepulse

NT_SERVER_ADDRESS = config("NT_SERVER_ADDRESS", default = "0.0.0.0")
LIGHTS_MODE_TOPIC_NAME = config("LIGHTS_MODE_TOPIC_NAME", default = "/SmartDashboard/Robot/Lights/Mode")
BOARD_PIN = board.D18
LIGHTS_COUNT = 150
BRIGHTNESS = 1
PIXEL_ORDER = neopixel.GRB

nt = ntcore.NetworkTableInstance.getDefault()
nt.startClient4("coproc-robot-lights")
nt.setServer(NT_SERVER_ADDRESS, ntcore.NetworkTableInstance.kDefaultPort4)

lightsModeTopic = nt.getStringTopic(LIGHTS_MODE_TOPIC_NAME).subscribe("DEFAULT")
lightsMode = "DEFAULT"

colorHotPink = color.calculate_intensity((150, 0, 10), 1)

pixels = neopixel.NeoPixel(BOARD_PIN, LIGHTS_COUNT, brightness=BRIGHTNESS, auto_write=False, pixel_order=PIXEL_ORDER)

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