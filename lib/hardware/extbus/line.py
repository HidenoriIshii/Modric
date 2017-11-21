# -*- coding: utf-8 --
# GPIO Lib
import pigpio

class Line():
    # AttrDir: output/input
    # AttrPud: pudup/puddw/pudoff
    # AttrInit: high/low
    # callback: func
    def __init__(self,gpio_no=0,AttrDir='output',AttrPud='pudoff',AttrInit='low'):
        print(gpio_no,AttrDir,AttrPud,AttrInit)
        self.pi = pigpio.pi()
        self.gpio = gpio_no
        self.init = AttrInit
        if AttrDir == 'output':
            self.pi.set_mode(self.gpio,pigpio.OUTPUT)
            if AttrInit == 'low':
                self.pi.write(self.gpio,0)
            else:self.pi.write(self.gpio,1)
                
        else:
            self.pi.set_mode(self.gpio,pigpio.INPUT)
        if AttrPud=='pudup':
            self.pi.set_pull_up_down(self.gpio,pigpio.PUD_UP)
        elif AttrPud=='puddw':
            self.pi.set_pull_up_down(self.gpio,pigpio.PUD_DOWN)
        elif AttrPud=='pudoff':
            self.pi.set_pull_up_down(self.gpio,pigpio.PUD_OFF)
        else:
            self.pi.set_pull_up_down(self.gpio,pigpio.PUD_DOWN)

    def getState(self):
        state = self.pi.read(self.gpio)
        if self.pi.read(self.gpio)== 0:
            return 'Low'
        else: return 'High'
    def setHigh(self):
        self.pi.write(self.gpio,1)
    def setLow(self):
        self.pi.write(self.gpio,0)
    def cleanup(self):
        if self.init == 'low':
            self.pi.write(self.gpio,0)
        else:self.pi.write(self.gpio,1)
