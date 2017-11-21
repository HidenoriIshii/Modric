# -*- coding: utf-8 -*-
# Single turn cermet trimmers 
from mcp3004_8 import Mcp3004_8

class Gf063():
    def __init__(self,adcch=0):
        # ADC Channel :0
        self.AdcCh = adcch
        self.Adc = Mcp3004_8() 
    def getAdcData(self):
        return self.Adc.transfer(self.AdcCh)
    def cleanup(self):
        self.Adc.cleanup()
