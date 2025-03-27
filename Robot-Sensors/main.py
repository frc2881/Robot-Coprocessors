import atexit
import board
import busio
import time
from ntcore import NetworkTableInstance, PubSubOptions
from adafruit_tca9548a import TCA9548A
from adafruit_vl53l4cd import VL53L4CD

nt = NetworkTableInstance.getDefault()
nt.startClient4("coproc-robot-sensors")
nt.setServer("10.28.81.2", NetworkTableInstance.kDefaultPort4)

distanceSensorGripperTopic = nt.getDoubleTopic(
  "/SmartDashboard/Robot/Sensors/Distance/Gripper/Value"
).publish(
  PubSubOptions(periodic=0.01)
)
distanceSensorGripperTopic.setDefault(-1.0)

distanceSensorIntakeTopic = nt.getDoubleTopic(
  "/SmartDashboard/Robot/Sensors/Distance/Intake/Value"
).publish(
  PubSubOptions(periodic=0.01)
)
distanceSensorIntakeTopic.setDefault(-1.0)

def onExit():
  distanceSensorGripperTopic.set(-1.0)
  distanceSensorIntakeTopic.set(-1.0)

atexit.register(onExit)

i2c = busio.I2C(board.I2C5_SCL, board.I2C5_SDA)
tca = TCA9548A(i2c)

distanceSensorGripper = None
distanceSensorIntake = None

try:
  distanceSensorGripper = VL53L4CD(tca[0])
  distanceSensorGripper.inter_measurement = 0
  distanceSensorGripper.timing_budget = 10
  distanceSensorGripper.start_ranging()

  distanceSensorIntake = VL53L4CD(tca[1])
  distanceSensorIntake.inter_measurement = 0
  distanceSensorIntake.timing_budget = 10
  distanceSensorIntake.start_ranging()
except:
  pass

while True:
  if nt.isConnected():
    if distanceSensorGripper is not None:
      if distanceSensorGripper.data_ready:
        distanceGripper = distanceSensorGripper.distance * 10
        distanceSensorGripper.clear_interrupt()
        distanceSensorGripperTopic.set(distanceGripper if distanceGripper > 0 else -1)

    if distanceSensorIntake is not None:
      if distanceSensorIntake.data_ready:
        distanceIntake = distanceSensorIntake.distance * 10
        distanceSensorIntake.clear_interrupt()
        distanceSensorIntakeTopic.set(distanceIntake if distanceIntake > 0 else -1)
  else:
    time.sleep(1)
