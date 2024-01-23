from decouple import config
import ntcore
import board
import adafruit_tca9548a
import adafruit_vl53l4cd

NT_SERVER_ADDRESS = config("NT_SERVER_ADDRESS", default = "0.0.0.0")
DISTANCE_SENSOR_1_TOPIC_NAME = config("DISTANCE_SENSOR_1_TOPIC_NAME", default = "/SmartDashboard/Robot/Sensor/Distance/1")
DISTANCE_SENSOR_1_PORT = config("DISTANCE_SENSOR_1_PORT", default = 0, cast = int)

nt = ntcore.NetworkTableInstance.getDefault()
nt.startClient4("coproc-robot-sensors")
nt.setServer(NT_SERVER_ADDRESS, ntcore.NetworkTableInstance.kDefaultPort4)

distanceSensor1Topic = nt.getDoubleTopic(DISTANCE_SENSOR_1_TOPIC_NAME).publish()
distanceSensor1Topic.setDefault(-1)

i2c = board.I2C()
tca = adafruit_tca9548a.TCA9548A(i2c)

distanceSensor1 = adafruit_vl53l4cd.VL53L4CD(tca[DISTANCE_SENSOR_1_PORT])
distanceSensor1.timing_budget = 20
distanceSensor1.start_ranging()

while True:
  if distanceSensor1.data_ready:
    distanceSensor1.clear_interrupt()
    distance = distanceSensor1.distance
    distanceSensor1Topic.set(distance if distance > 0 else -1)
