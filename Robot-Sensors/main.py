import atexit
import board
import time
import ntcore
import adafruit_tca9548a
import adafruit_vl53l4cd

nt = ntcore.NetworkTableInstance.getDefault()
nt.startClient4("coproc-robot-sensors")
nt.setServer("10.28.81.2", ntcore.NetworkTableInstance.kDefaultPort4)

distanceSensorIntakeTopic = nt.getDoubleTopic("/SmartDashboard/Robot/Sensor/Distance/Intake").publish()
distanceSensorIntakeTopic.setDefault(-1)

distanceSensorLauncherTopic = nt.getDoubleTopic("/SmartDashboard/Robot/Sensor/Distance/Launcher").publish()
distanceSensorLauncherTopic.setDefault(-1)

def onExit():
  distanceSensorIntakeTopic.set(-1)
  distanceSensorLauncherTopic.set(-1)

atexit.register(onExit)

i2c = board.I2C()
tca = adafruit_tca9548a.TCA9548A(i2c)

distanceSensorIntake = adafruit_vl53l4cd.VL53L4CD(tca[0])
distanceSensorIntake.inter_measurement = 0
distanceSensorIntake.timing_budget = 10
distanceSensorIntake.start_ranging()

distanceSensorLauncher = adafruit_vl53l4cd.VL53L4CD(tca[1])
distanceSensorLauncher.inter_measurement = 0
distanceSensorLauncher.timing_budget = 10
distanceSensorLauncher.start_ranging()

while True:
  if nt.isConnected():
    if distanceSensorIntake.data_ready:
      distanceIntake = distanceSensorIntake.distance * 10
      distanceSensorIntake.clear_interrupt()
      distanceSensorIntakeTopic.set(distanceIntake if distanceIntake > 0 else -1)
    if distanceSensorLauncher.data_ready:
      distanceLauncher = distanceSensorLauncher.distance * 10
      distanceSensorLauncher.clear_interrupt()
  else:
    time.sleep(1)
