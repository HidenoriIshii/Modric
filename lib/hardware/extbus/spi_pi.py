# -*- coding: utf-8 -*-
#Spi Lib
import pigpio 

class Spi():
    '''
    ch: ch 0-2
    mode:
      0:POL0 PHA1
      1:POL0 PHA1
      2:POL1 PHA0
      3:POL1 PHA1
    '''
    def __init__(self,spi_ch=0,mode=0,speed=1000000,bits_word=8):
        self.CpuSpi = pigpio.pi()
        '''    
        mode:
         0:POL0 PHA1
         1:POL0 PHA1
         3:POL1 PHA1
        '''
        self.mode = mode
        self.speed = speed
        self.spi_ch = spi_ch
        self.bits = bits_word
        flag = self.mode 
        self.handle = -1
        print(self.spi_ch,self.speed,self.mode,self.bits)
        self.open()
    def open(self):    
        flag = self.mode 
        self.handle = self.CpuSpi.spi_open(self.spi_ch,self.speed,flag)
    def transfer(self,send_data,count=0):
        (count,data) = self.CpuSpi.spi_xfer(self.handle,send_data)
        return data
    def close(self):
        try:
            self.CpuSpi.spi_close(self.handle)
        except AttributeError:
            pass
        self.handle = -1
    def cleanup(self):
        self.close()
        self.pi.stop()
