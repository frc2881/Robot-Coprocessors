#!/usr/bin/env python3

import os
import time
import re
from decouple import config
from smartcard.CardMonitoring import CardMonitor, CardObserver
import ntcore

NT_SERVER_ADDRESS = config("NT_SERVER_ADDRESS", default = "0.0.0.0")
BATTERY_INFO_TOPIC_NAME = config("BATTERY_INFO_TOPIC_NAME", default = "/SmartDashboard/Robot/Battery/Info")

batteryInfo = "UNKNOWN"

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

nt = ntcore.NetworkTableInstance.getDefault()
nt.startClient4("coproc-robot-batteryinfo")
nt.setServer(NT_SERVER_ADDRESS, ntcore.NetworkTableInstance.kDefaultPort4)
topic = nt.getStringTopic(BATTERY_INFO_TOPIC_NAME).publish()

while True:
  topic.set(batteryInfo)
  time.sleep(10)