from decouple import config
import ntcore
import board
import adafruit_tca9548a
import adafruit_vl53l4cd

NT_SERVER_ADDRESS = config("NT_SERVER_ADDRESS", default = "0.0.0.0")
DISTANCE_SENSOR_INTAKE_TOPIC_NAME = config("DISTANCE_SENSOR_INTAKE_TOPIC_NAME", default = "/SmartDashboard/Robot/Sensor/Distance/Intake")
DISTANCE_SENSOR_INTAKE_PORT = config("DISTANCE_SENSOR_INTAKE_PORT", default = 0, cast = int)

nt = ntcore.NetworkTableInstance.getDefault()
nt.startClient4("coproc-robot-sensors")
nt.setServer(NT_SERVER_ADDRESS, ntcore.NetworkTableInstance.kDefaultPort4)

distanceSensorIntakeTopic = nt.getDoubleTopic(DISTANCE_SENSOR_INTAKE_TOPIC_NAME).publish()
distanceSensorIntakeTopic.setDefault(-1)

i2c = board.I2C()
tca = adafruit_tca9548a.TCA9548A(i2c)

distanceSensorIntake = adafruit_vl53l4cd.VL53L4CD(tca[DISTANCE_SENSOR_INTAKE_PORT])
distanceSensorIntake.timing_budget = 20
distanceSensorIntake.start_ranging()

while True:
  if distanceSensorIntake.data_ready:
    distanceSensorIntake.clear_interrupt()
    distance = distanceSensorIntake.distance
    distanceSensorIntakeTopic.set(distance if distance > 0 else -1)
