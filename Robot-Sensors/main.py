import atexit
from board import I2C
import time
from ntcore import NetworkTableInstance, PubSubOptions
from adafruit_tca9548a import TCA9548A
from adafruit_vl53l4cd import VL53L4CD

nt = NetworkTableInstance.getDefault()
nt.startClient4("coproc-robot-sensors")
nt.setServer("10.28.81.2", NetworkTableInstance.kDefaultPort4)

distanceSensorIntakeTopic = nt.getDoubleTopic(
  "/SmartDashboard/Robot/Sensors/Distance/Intake/Value"
).publish(
  PubSubOptions(periodic=0.01)
)
distanceSensorIntakeTopic.setDefault(-1.0)

distanceSensorLauncherTopic = nt.getDoubleTopic(
  "/SmartDashboard/Robot/Sensors/Distance/Launcher/Value"
).publish(
  PubSubOptions(periodic=0.01)
)
distanceSensorLauncherTopic.setDefault(-1.0)

distanceSensorClimberTopic = nt.getDoubleTopic(
  "/SmartDashboard/Robot/Sensors/Distance/Climber/Value"
).publish(
  PubSubOptions(periodic=0.01)
)
distanceSensorClimberTopic.setDefault(-1.0)

def onExit():
  distanceSensorIntakeTopic.set(-1.0)
  distanceSensorLauncherTopic.set(-1.0)
  distanceSensorClimberTopic.set(-1.0)

atexit.register(onExit)

i2c = I2C()
tca = TCA9548A(i2c)

distanceSensorIntake = None
try:
  distanceSensorIntake = VL53L4CD(tca[0])
  distanceSensorIntake.inter_measurement = 0
  distanceSensorIntake.timing_budget = 10
  distanceSensorIntake.start_ranging()
except:
  pass

distanceSensorLauncher = None
try:
  distanceSensorLauncher = VL53L4CD(tca[1])
  distanceSensorLauncher.inter_measurement = 0
  distanceSensorLauncher.timing_budget = 10
  distanceSensorLauncher.start_ranging()
except:
  pass

distanceSensorClimber = None
try:
  distanceSensorClimber = VL53L4CD(tca[2])
  distanceSensorClimber.inter_measurement = 0
  distanceSensorClimber.timing_budget = 10
  distanceSensorClimber.start_ranging()
except:
  pass

while True:
  if nt.isConnected():
    if distanceSensorIntake is not None:
      if distanceSensorIntake.data_ready:
        distanceIntake = distanceSensorIntake.distance * 10
        distanceSensorIntake.clear_interrupt()
        distanceSensorIntakeTopic.set(distanceIntake if distanceIntake > 0 else -1)
    if distanceSensorLauncher is not None:
      if distanceSensorLauncher.data_ready:
        distanceLauncher = distanceSensorLauncher.distance * 10
        distanceSensorLauncher.clear_interrupt()
        distanceSensorLauncherTopic.set(distanceLauncher if distanceLauncher > 0 else -1)
    if distanceSensorClimber is not None:
      if distanceSensorClimber.data_ready:
        distanceClimber = distanceSensorClimber.distance * 10
        distanceSensorClimber.clear_interrupt()
        distanceSensorClimberTopic.set(distanceClimber if distanceClimber > 0 else -1)
  else:
    time.sleep(1)
