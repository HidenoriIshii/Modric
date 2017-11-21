# -*- coding: utf-8 -*-
# MCP3004/3008 series
#import sys
#sys.path.append('../extbus')
from spi_pi import Spi
from time import sleep
#from spi import Spi
class Mcp3004_8():
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
        self.Vdd =3.3 
        #step:1023(Duty 0%:0 Duty 100%:1023)
        self.step = 1023
        #mode Single
        self.mode = 1<<7
        self.extbus = Spi(spi_ch=0,mode=self.mode,speed=self.speed,bits_word=8)
    def transfer(self,adc_ch=0):
        # 1byte:start bit
        send_data1 = 0x01
        # 2byte:SGL/DIFF+ CH
        send_data2 = ((self.mode + adc_ch<<4)&0xf0)
        # 3byte:dummy
        dummy_data = 0xff
        send_data = [send_data1,send_data2,dummy_data]
        recv_data = [0,0]
        recv_data = self.extbus.transfer(send_data,3)
        val_ad= (((recv_data[1] & 0x03)<< 8) + recv_data[2])
        #wait 1.5 clock(1.6ns) over
        #0.001s:1ms. 0.0001s:1ns
	sleep(0.0002)
	return val_ad
    def getVin(self,data):
        '''
            data = ( steps * VIN ) / VDD
            VIN:analog input voltage
            VDD:supply voltage
            VIN = (data * VDD) / steps
        '''
        voltage = float(data * self.Vdd)  / self.step
        return voltage
    def cleanup(self):
        self.extbus.close()
