# -*- coding: utf-8 -*-
from bob09110 import Bob09110
from sw import Sw
class JoyStick():
    def __init__(self,adcch_vert=0,adcch_horz=1,gpiono_sel=2):
        self.adcdev = Bob09110(adcch_vert,adcch_horz)
        self.sw = Sw(gpiono_sel,'pudup')
    def getValVert(self):
        return self.adcdev.getValVert()
    def getValHorz(self):
        return self.adcdev.getValHorz()
    def getSelState(self):
        return (self.sw.getState())
    def getRowDataVert(self):
        return self.adcdev.getRowDataVert()
    def getRowDataHorz(self):
        return self.adcdev.getRowDataHorz()
    def cleanup(self):
        self.adcdev.cleanup()
        self.sw.cleanup()
