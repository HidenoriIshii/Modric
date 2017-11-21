#-*- coding: utf-8 -*-
from line import Line
class Led():
    def __init__(self,pin_no):
        self.line = Line(pin_no,'output','low')        
    def getState(self):
        state = self.line.getState()
        if state == 'Low':
            return 'Off'
        else:
            return 'On'
    def setLedOn(self):
        self.line.setHigh()
    def setLedOff(self):
        self.line.setLow()
    def cleanup(self):
        self.setLedOff()
        self.line.cleanup()
