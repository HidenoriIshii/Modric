# -*- coding: utf-8 -*-
from pca9685 import Pca9685
class I2cServo():
    _I2CSERVO_HORZ_0 = 1
    _I2CSERVO_VERT_0 = 0
    _I2CSERVO_VOL_0 = 2
    def __init__(self,deg_max=180,deg_min=0):
        self.dev = Pca9685()
        # duty_cnt = duty(%)/100(%)*4095
        #          = (duty * 4095) / 100 
        self.servomin = 144
        self.servomax = 749 
        self.servocenter = 276
        self.dev.setPwmDuty(self._I2CSERVO_HORZ_0,self.servocenter)
        self.dev.setPwmDuty(self._I2CSERVO_VERT_0,self.servocenter)
        self.dev.setPwmDuty(self._I2CSERVO_VOL_0,self.servocenter)
    
    def setPWMFreq(self,freq):
        self.dev.setPWMFreq(freq)
    def setAdValtoDuty(self,pwmch,val,val_min,val_max):
        duty = int(((self.servomax-self.servomin)*(val-val_min)) / (val_max-val_min)) + self.servomin
        self.dev.setPwmDuty(pwmch,duty)
    def setDuty(self,pwmch,duty):
        if duty < self.servomin: duty=self.servomin
        elif duty> self.servomax:duty = self.servomax
        self.dev.setPwmDuty(pwmch,duty)

    def getDuty(self,pwmch):
        return self.dev.getPwmDuty(pwmch)
    def cleanup(self):
        self.dev.setPwmDuty(self._I2CSERVO_HORZ_0,self.servocenter)
        self.dev.setPwmDuty(self._I2CSERVO_VERT_0,self.servocenter)
        self.dev.setPwmDuty(self._I2CSERVO_VOL_0,self.servocenter)
	self.dev.cleanup()
