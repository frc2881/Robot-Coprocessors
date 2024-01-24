from decouple import config
import ntcore
import time

NT_SERVER_ADDRESS = config("NT_SERVER_ADDRESS", default = "0.0.0.0")
LIGHTS_MODE_TOPIC_NAME = config("LIGHTS_MODE_TOPIC_NAME", default = "/SmartDashboard/Robot/Lights/Mode")

nt = ntcore.NetworkTableInstance.getDefault()
nt.startClient4("coproc-robot-lights")
nt.setServer(NT_SERVER_ADDRESS, ntcore.NetworkTableInstance.kDefaultPort4)

lightsModeTopic = nt.getStringTopic(LIGHTS_MODE_TOPIC_NAME).subscribe()

# TODO: implement all the light control things!

while True:
  print(lightsModeTopic.get())
  time.sleep(0.02)
