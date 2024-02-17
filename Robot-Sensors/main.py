from decouple import config
import atexit
import time
import ntcore
import board
import adafruit_tca9548a
import adafruit_vl53l4cd

NT_SERVER_ADDRESS = config("NT_SERVER_ADDRESS", default = "10.28.81.2")
DISTANCE_SENSOR_INTAKE_TOPIC_NAME = config("DISTANCE_SENSOR_INTAKE_TOPIC_NAME", default = "/SmartDashboard/Robot/Sensor/Distance/Intake")
DISTANCE_SENSOR_INTAKE_PORT = config("DISTANCE_SENSOR_INTAKE_PORT", default = 0, cast = int)
DISTANCE_SENSOR_LAUNCHER_TOPIC_NAME = config("DISTANCE_SENSOR_LAUNCHER_TOPIC_NAME", default = "/SmartDashboard/Robot/Sensor/Distance/Launcher")
DISTANCE_SENSOR_LAUNCHER_PORT = config("DISTANCE_SENSOR_LAUNCHER_PORT", default = 1, cast = int)

nt = ntcore.NetworkTableInstance.getDefault()
nt.startClient4("coproc-robot-sensors")
nt.setServer(NT_SERVER_ADDRESS, ntcore.NetworkTableInstance.kDefaultPort4)

distanceSensorIntakeTopic = nt.getDoubleTopic(DISTANCE_SENSOR_INTAKE_TOPIC_NAME).publish()
distanceSensorIntakeTopic.setDefault(-1)

distanceSensorLauncherTopic = nt.getDoubleTopic(DISTANCE_SENSOR_LAUNCHER_TOPIC_NAME).publish()
distanceSensorLauncherTopic.setDefault(-1)

i2c = board.I2C()
tca = adafruit_tca9548a.TCA9548A(i2c)

distanceSensorIntake = adafruit_vl53l4cd.VL53L4CD(tca[DISTANCE_SENSOR_INTAKE_PORT])
distanceSensorIntake.inter_measurement = 0
distanceSensorIntake.timing_budget = 10
distanceSensorIntake.start_ranging()

distanceSensorLauncher = adafruit_vl53l4cd.VL53L4CD(tca[DISTANCE_SENSOR_LAUNCHER_PORT])
distanceSensorLauncher.inter_measurement = 0
distanceSensorLauncher.timing_budget = 10
distanceSensorLauncher.start_ranging()

def onExit():
  distanceSensorIntakeTopic.set(-1)
  distanceSensorLauncherTopic.set(-1)
  distanceSensorIntake.stop_ranging()
  distanceSensorLauncher.stop_ranging()

atexit.register(onExit)

while True:
  if nt.isConnected():
    if distanceSensorIntake.data_ready:
      distanceIntake = distanceSensorIntake.distance
      distanceSensorIntakeTopic.set(distanceIntake if distanceIntake > 0 else -1)
      distanceSensorIntake.clear_interrupt()
    if distanceSensorLauncher.data_ready:
      distanceLauncher = distanceSensorLauncher.distance
      distanceSensorLauncherTopic.set(distanceLauncher if distanceLauncher > 0 else -1)
      distanceSensorLauncher.clear_interrupt()
  else:
    time.sleep(1)
