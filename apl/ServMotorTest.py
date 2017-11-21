# -*- coding: utf-8 -*-

import sys
sys.path.append('../lib/base')
sys.path.append('../gui')
sys.path.append('../lib/hardware/extbus')
sys.path.append('../lib/hardware/device')
from servmotor import ServMotor
# TIME Lib
import time
#GUI Lib
import Tkinter as tk
import wiringpi as w

class ServMotorTest():
    def __init__(self):
        # ServMotor  instanse
        self.sm = ServMotor(18,180,0)       
    def cleanup(self):
        print 'Test Finished'
        self.js.cleanup()
        try:
            self.led.cleanup()
        except RuntimeWarning:
            pass
        sys.exit()
    def test(self):
        while 1:
            for deg in range(0,181,10):
                self.sm.setDeg(float(deg))
                #Wait 0.5sec
                time.sleep(0.5)
                freq = self.sm.getFreq()
                duty = self.sm.getDuty()
                print 'freq:%d'% freq,'duty:%d'% duty
            for deg in range(180,-1,-10):
                self.sm.setDeg(float(deg))
                #wait 0.5sec
                time.sleep(0.5)
                freq = self.sm.getFreq()
                duty = self.sm.getDuty()
                print 'freq:%d'% freq,'duty:%d'% duty
    def cleanup(self):
        self.sm.cleanup()
        sys.exit

if __name__ == '__main__':
    root = tk.Tk()
    App = ServMotorTest()
    try:
        App.test()
    except KeyboardInterrupt:
        pass
    App.cleanup()
    pass
