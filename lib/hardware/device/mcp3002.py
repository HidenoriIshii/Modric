# -*- coding: utf-8 -*-

import sys
sys.path.append('../extbus')
from spi_pi import Spi
#from spi import Spi
class Mcp3002():
    '''
     mode :0 CPOL:0 CPHA:0
     mode :1 CPOL:0 CPHA:1
     mode :2 CPOL:1 CPHA:0
     mode :3 CPOL:1 CPHA:1

    '''
    def __init__(self):
        #device_no
        self.device_no = 0
        #Max speed:3.2MHz(5V)
        #self.speed = 3200000
        #self.Vdd = 5.0
        #Max speed:1.2MHz(3.3V)
        self.speed = 1200000
        self.Vdd = 3.3
        #step:1023(Duty 0%:0 Duty 100%:1023)
        self.step = 1023
        #mode Single
        self.mode = 1
        #MSB
        self.msbf = 1
        self.extbus = Spi(spi_ch=0,mode=self.mode,speed=self.speed,bits_word=8)
    def transfer(self,adc_ch=0):
        startbit = 1<<6
        mode= self.mode<<5
        msbf= self.msbf<<3
        send_data = 0x00
        send_data |= (startbit + mode + adc_ch + msbf)
        dummy_data = 0xff
        send_data = [send_data,dummy_data]
        recv_data = [0,0]
        recv_data = self.extbus.transfer(send_data,2)
        val_ad= (((recv_data[0] & 0x03)<< 8) + recv_data[1])
        return val_ad
    def getVin(self,data):
        '''
            data = ( 1023 * VIN ) / VDD
            VIN:analog input voltage
            VDD:supply voltage
            VIN = (data * VDD) / 1023
        '''
        voltage = (data * self.Vdd)  / self.step
        #0.0V: 512
        voltage -= 512
        return voltage
    def cleanup(self):
        self.extbus.close()
