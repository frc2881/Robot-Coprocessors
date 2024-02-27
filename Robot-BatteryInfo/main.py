import os
import time
import re
import ntcore
from smartcard.CardMonitoring import CardMonitor, CardObserver

nt = ntcore.NetworkTableInstance.getDefault()
nt.startClient4("coproc-robot-batteryinfo")
nt.setServer("10.28.81.2", ntcore.NetworkTableInstance.kDefaultPort4)

batteryInfo = "UNKNOWN"

batteryInfoTopic = nt.getStringTopic("/SmartDashboard/Robot/Power/Battery/Info").publish()
batteryInfoTopic.setDefault(batteryInfo)

class CardTransmitObserver(CardObserver):
  def update(self, observable, actions):
    global batteryInfo
    (addedcards, removedcards) = actions
    for card in addedcards:
      card.connection = card.createConnection()
      card.connection.connect()
      data = []
      for i in range(0, 32):
        block, sw1, sw2 = card.connection.transmit([0xFF, 0xB0, 0x00, i, 4])
        data += block
        if 254 in block:
          break
      batteryInfo = re.search("T\x02en(.*)þ", u"".join(u"".join(map(chr, data)).split())).groups()[0]
      card.connection.disconnect()
    for card in removedcards:
      batteryInfo = "UNKNOWN"

os.system("service pcscd restart")

monitor = CardMonitor()
observer = CardTransmitObserver()
monitor.addObserver(observer)

while True:
  if nt.isConnected():
    batteryInfoTopic.set(batteryInfo)
    time.sleep(5)
  else:
    time.sleep(1)