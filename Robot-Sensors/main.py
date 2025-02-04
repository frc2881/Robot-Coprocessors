import atexit
import busio
import time
from ntcore import NetworkTableInstance, PubSubOptions
from adafruit_tca9548a import TCA9548A
from adafruit_vl53l4cd import VL53L4CD

nt = NetworkTableInstance.getDefault()
nt.startClient4("coproc-robot-sensors")
nt.setServer("10.28.81.2", NetworkTableInstance.kDefaultPort4)

distanceSensorLauncherTopic = nt.getDoubleTopic(
  "/SmartDashboard/Robot/Sensors/Distance/Launcher/Value"
).publish(
  PubSubOptions(periodic=0.01)
)
distanceSensorLauncherTopic.setDefault(-1.0)

def onExit():
  distanceSensorLauncherTopic.set(-1.0)

atexit.register(onExit)

i2c = busio.I2C(board.I2C5_SCL, board.I2C5_SDA)
tca = TCA9548A(i2c)

distanceSensorLauncher = None
try:
  distanceSensorLauncher = VL53L4CD(tca[0])
  distanceSensorLauncher.inter_measurement = 0
  distanceSensorLauncher.timing_budget = 10
  distanceSensorLauncher.start_ranging()
except:
  pass

while True:
  if nt.isConnected():
    if distanceSensorLauncher is not None:
      if distanceSensorLauncher.data_ready:
        distanceLauncher = distanceSensorLauncher.distance * 10
        distanceSensorLauncher.clear_interrupt()
        distanceSensorLauncherTopic.set(distanceLauncher if distanceLauncher > 0 else -1)
  else:
    time.sleep(1)