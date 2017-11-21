# -*- coding: utf-8 -*-
# PIGPIO Lib
import pigpio

class Pwm():
    #freq: Hz
    #duty:0-range
    #duty_range:251-40000(default:255)
    def __init__(self,gpio_no=0,freq=0,duty=0,duty_range=255):
        self.CpuPwm = pigpio.pi()
        self.gpio = gpio_no
        self.freq = freq
        self.duty = duty
        self.duty_range = duty_range
        self.CpuPwm.set_mode(self.gpio,pigpio.OUTPUT)
        self.CpuPwm.set_PWM_frequency(self.gpio,self.freq)
        self.CpuPwm.set_PWM_range(self.gpio,self.duty_range)
    def start(self,duty):
        self.CpuPwm.set_mode(self.gpio,pigpio.OUTPUT)
        self.CpuPwm.set_PWM_frequency(self.gpio,self.freq)
    def stop(self):
        self.duty = 0
        self.CpuPwm.set_PWM_frequency(self.gpio,0)
        self.CpuPwm.set_mode(self.gpio,pigpio.INPUT)
    #freq:Hz
    def setFreq(self,freq):
        self.freq = freq
        self.CpuPwm.ChangeFrequency(freq)
    def getFreq(self):
        return self.CpuPwm.get_PWM_frequency(self.gpio)
    #duty:0.0-duty_range
    def setDuty(self,duty):
        self.duty = duty
        self.CpuPwm.set_PWM_dutycycle(self.gpio,self.duty)
    def getDuty(self):
        return self.CpuPwm.get_PWM_dutycycle(self.gpio)
    def cleanup(self):
        self.stop()
        self.pi.stop()
