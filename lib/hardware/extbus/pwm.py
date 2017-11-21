# -*- coding: utf-8 -*-
# GPIO Lib
import RPi.GPIO as GPIO

class Pwm():
    #freq: Hz
    #duty:0.0-100.0 %
    def __init__(self,pin_no=0,freq=0,duty=0):
        self.pin = pin_no
        self.freq = freq
        self.duty = duty
        try:
            GPIO.setup(self.pin,GPIO.OUT,initial=GPIO.LOW)
        except RuntimeWarning:
            pass
        self.CpuPwm = GPIO.PWM(self.pin,self.freq)
    def start(self,duty):
        self.CpuPwm.start(duty)
    def stop(self):
        self.CpuPwm.stop()
    #freq:Hz
    def setFreq(self,freq):
        self.freq = freq
        self.CpuPwm.ChangeFrequency(freq)
    #duty:0.0-100.0 %
    def setDuty(self,duty):
        self.duty = duty
        self.CpuPwm.ChangeDutyCycle(self.duty)
    def cleanup(self):
        GPIO.cleanup(self.pin)
