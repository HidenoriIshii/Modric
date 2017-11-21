# -*- coding: utf-8 -*-
# Cds cell
from mcp3002 import Mcp3002

class Mi5():
    def __init__(self):
        # ADC Channel :0
        self.AdcCh = 1<<4
        self.Adc = Mcp3002() 
    def readVolt(self):
        data = self.Adc.transfer(self.AdcCh)
        return self.Adc.getVin(data)
    def cleanup(self):
        self.Adc.cleanup()
