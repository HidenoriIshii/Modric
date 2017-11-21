# -*- coding: utf-8 -*-

import sys
sys.path.append('../lib/base')
sys.path.append('../gui')
sys.path.append('../lib/hardware/extbus')
sys.path.append('../lib/hardware/device')
from volume import Volume
from lightsens import LightSens
# TIME Lib
import time

class AdcDevTest():
    def __init__(self):
        self.volt_vol = 0
        self.volt_ls = 0
        self.vol = Volume(0)
#        self.ls = LightSens()
    def VoltageTest(self):
        self.volt_vol = self.vol.getValVol()
#        self.volt_ls = self.ls.getVolt()
        print ('Volume(V)= %d' % self.volt_vol)
 #               'LightSens(V)= %2.2f' % self.volt_ls
        time.sleep(0.5)
    def cleanup(self):
        self.vol.cleanup()
 #       self.ls.cleanup()
if __name__ == '__main__':
    print "Adc Test"
    test = AdcDevTest()
    test.VoltageTest()
    test.VoltageTest()
    test.VoltageTest()
    test.cleanup()
    pass



