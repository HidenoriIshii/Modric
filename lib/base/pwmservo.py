# -*- coding: utf-8 -*-
from pwm_pi import Pwm
#from pwm import Pwm
class PwmServo():
    def __init__(self,gpio_no,deg_max=180,deg_min=0):
        self.pwm = Pwm(gpio_no,100,0,255)
        self.degmax = deg_max
        self.degmin = deg_min
        #duty
        self.dutymax = 56.0 
        self.dutymin = 12.0
        self.deg = 0
    def start(self):
        self.pwm.start(0)
    def stop(self):
        self.pwm.stop()
        self.pwm.setDuty()
    def setDeg(self,deg):
        self.deg = deg
        duty = (((deg-self.degmin) * ((self.dutymax -self.dutymin) /\
                (self.degmax-self.degmin)))+self.dutymin)
#        print 'deg:%d'% deg,'duty:%d'% duty
        self.pwm.setDuty(duty)
    def getDeg(self):
        return self.deg
    def cleanup(self):
        self.pwm.stop()
        self.pwm.cleanup()
    def getFreq(self):
        return self.pwm.getFreq()
    def getDuty(self):
        return self.pwm.getDuty()
