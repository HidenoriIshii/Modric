# -*- coding: utf-8 -*-
import sys
sys.path.append('../lib/hardware/device')
from mi5 import Mi5

class LightSens():
    def __init__(self):
        self.intensityLv = 0
        self.device = Mi5()
    def getVolt(self):
        volt = self.device.readVolt()
        return volt
    def cleanup(self):
        self.device.cleanup()
