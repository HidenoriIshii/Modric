# -*- coding: utf-8 -*-
#I2C Lib
import pigpio 

class I2c():
    '''
    bus:
        0:
        1:Raspberry Pi2 ModelB(SDA1,SCL1)
    '''
    def __init__(self,addr=0x40,bus=1):
        self.handle = -1
        self.pi= pigpio.pi()
        self.open(addr,bus)        
    def open(self,addr,bus):
        self.handle = self.pi.i2c_open(bus,addr)
    def recvbyte(self,reg):
        data = self.pi.i2c_read_byte_data(self.handle,reg)
        return data
    def sendbyte(self,reg,data):
        self.pi.i2c_write_byte_data(self.handle,reg,data)
    def sendbytes(self,reg,data):
        self.pi.i2c_write_i2c_block_data(self.handle,reg,data)
    def close(self):
        try:
            self.pi.I2c_close(self.handle)
        except AttributeError:
            pass
        self.handle = -1
    def cleanup(self):
        self.close()
        self.pi.stop()
