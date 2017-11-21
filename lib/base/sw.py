# -*- coding: utf-8 -*-
from line import Line
import pigpio
class Sw():
    # pud :pudup,puddw,pudoff
    # edge : either,rising,filling
    def __init__(self,gpio_no,pud='pudup'):
        self.line = Line(gpio_no,'input',pud,'high')
        linestate = self.line.getState()
        if linestate == 'High': self.state = 'Released'
        else:self.state = 'Pressed'
    def getState(self):
        linestate = self.line.getState()
        if linestate == 'High': self.state = 'Released'
        else: self.state = 'Pressed'
        return self.state
    def cleanup(self):
        self.line.cleanup()
