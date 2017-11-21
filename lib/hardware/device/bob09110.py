# -*- coding: utf-8 -*-
# joyStick Device
#from mcp3002 import Mcp3002
from mcp3004_8 import Mcp3004_8
class Bob09110():
    def __init__(self,adcch_vert=0,adcch_horz=1):
        self.AdcChVert = adcch_vert
        self.AdcChHorz = adcch_horz
        self.Adc = Mcp3004_8()
        self.adcvert = 0
        self.adchorz = 0
    def getValVert(self):
        data = self.Adc.transfer(self.AdcChVert)
        self.adcvert = data
        return self.Adc.getVin(data)
    def getValHorz(self):
        data = self.Adc.transfer(self.AdcChHorz)
        self.adchorz = data
        return self.Adc.getVin(data)
    def getRowDataVert(self):
        return self.adcvert
    def getRowDataHorz(self):
        return self.adchorz
    def cleanup(self):
        self.Adc.cleanup()

