# -*- coding: utf-8 -*-
#Spi Lib
import spidev

class Spi():
    def __init__(self,spi_ch=0,mode=0,speed=100000,bits_word=8):
        self.CpuSpi = spidev.SpiDev()
        # SPI Bus used  onyly No. O. 
        self.mode = mode
        self.speed = speed
        self.spi_ch = spi_ch
        self.bits = bits_word
        print(self.spi_ch,self.speed,self.mode,self.bits)
        self.open()
    def open(self):
        self.CpuSpi.open(0,self.spi_ch)
        self.CpuSpi.max_speed_hz = self.speed
        self.CpuSpi.bits_per_word = self.bits
    def transfer(self,send_data,count):
        return self.CpuSpi.xfer2(send_data)
    def close(self):
        self.CpuSpi.close()
    def cleanup(self):
        self.CpuSpi.close()

