# -*- coding: utf-8 -*-
from gf063 import Gf063

class Volume():
    def __init__(self,adcch=0):
        self.AdcVol = 0
        self.device = Gf063(adcch)
    def getValVol(self):
        self.AdcVol = self.device.getAdcData()
        return self.AdcVol 
    def cleanup(self):
        self.device.cleanup()
