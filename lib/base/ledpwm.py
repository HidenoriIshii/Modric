# -*- coding: utf-8 -*-
from pwm_pi import Pwm

class LedPwm():
    def __init__(self,pin_no):
        self.pwm = Pwm(pin_no,100,0)
    def start(self):
        self.pwm.start(0)
        self.state = 'active'
    def seton(self):
        self.pwm.setDuty(100)
    def setoff(self):
        self.pwm.setDuty(0)
    def stop(self):
        self.pwm.stop()
    def setDuty(self,duty=0):
        self.pwm.setDuty(duty)
    def setFreq(self,ferq):
        self.pwm.setFreq(freq)
    def cleanup(self):
        self.pwm.stop()
        self.pwm.cleanup()
