# -*- coding: utf-8 -*-

#import sys
#sys.path.append('../extbus')
from i2c_pi import I2c
import time
class Pca9685():
    _REG_PCA9685_MODE1 = 0x00
    _REG_PCA9685_MODE2 = 0x01
    # H(period time of LED ON)
    _REG_PCA9685_LED0_ON_L  = 0x06
    _REG_PCA9685_LED0_ON_H  = 0x07
    _REG_PCA9685_LED0_OFF_L = 0x08
    _REG_PCA9685_LED0_OFF_H = 0x09
    _REG_PCA9685_PRESCALE= 0xFE

    #MODE1
    _MODE1_RESTART_DISABLE  = 0<<7 #default
    _MODE1_RESTART_ENABLE   = 1<<7 
    _MODE1_EXTCLK_INTERNAL_25M   = 0<<6 #default
    _MODE1_EXTCLK_EXTERNAL    = 1<<6
    _MODE1_AI_DISABLE       = 0<<5 #default
    _MODE1_AI_ENABLE        = 1<<5
    _MODE1_SLEEP_NORMAL     = 0<<4 
    _MODE1_SLEEP_LOWPOWER   = 1<<4 #default
    _MODE1_SUB1_DISABLE     = 0<<3 #default
    _MODE1_SUB1_ENABLE      = 1<<3
    _MODE1_SUB2_DISABLE     = 0<<2 #default
    _MODE1_SUB2_ENABLE      = 1<<2
    _MODE1_SUB3_DISABLE     = 0<<1 #default
    _MODE1_SUB3_ENABLE      = 1<<1
    _MODE1_ALLCALL_DISABLE  = 0<<0 
    _MODE1_ALLCALL_ENABLE   = 1<<0 #default
    #MODE2
    _MODE2_OCH_STOP         = 0<<3 #default
    _MODE2_OCH_ACK          = 1<<3
    _MODE2_OUTDRV_OPEN_DRAIN  = 0<<2
    _MODE2_OUTDRV_TOTEM       = 1<<2 # default
    
    def __init__(self):
        self.addr = 0x40
        self.bus = 1
        self.extbus = I2c(self.addr,self.bus)
        # PCA9685 restart
        data = self.read_reg(self._REG_PCA9685_MODE1)
        data |= self._MODE1_AI_ENABLE
        data |= self._MODE1_ALLCALL_ENABLE
        data &= ~self._MODE1_SUB3_ENABLE
        self.write_reg(self._REG_PCA9685_MODE1,data)
        data = self.read_reg(self._REG_PCA9685_MODE2)
        data |= (self._MODE2_OCH_ACK|self._MODE2_OUTDRV_TOTEM)
        self.write_reg(self._REG_PCA9685_MODE2,data)
        #wait 500us
        time.sleep(0.0005)
        data = self.read_reg(self._REG_PCA9685_MODE1)
        data |= (self._MODE1_RESTART_ENABLE|self._MODE1_EXTCLK_INTERNAL_25M)
        data &= ~self._MODE1_SLEEP_LOWPOWER
        self.write_reg(self._REG_PCA9685_MODE1,data)
        #wait 500us
        time.sleep(0.0005)
        data = self.read_reg(self._REG_PCA9685_MODE1)

    def write_regs(self,reg,data):
        self.extbus.sendbytes(reg,data)
    def write_reg(self,reg,data):
        self.extbus.sendbyte(reg,data)
    def read_reg(self,reg):
        return self.extbus.recvbyte(reg)
    #freq: 24Hz < freq < 1526Hz
    def setPWMFreq(self,freq):
        # PWM freq = SYSCLK / (4096 * (prescale + 1))
        # (4096 * (prescale + 1)) / SYSCLK =  1 / PWM freq
        # (4096 * (prescale + 1)) = SYSCLK  / PWM freq
        # (prescale + 1) = (SYSCLK  / PWM freq)/4096
        # prescale  = ((SYSCLK  / PWM freq)/4096) - 1
        #  SYSCLK = 25MHz = 25000000
        # prescale  = ((SYSCLK  / PWM freq)/4096) - 1
        if freq < 24:
            prescale = 254
        elif freq > 1526:
            prescale = 3
        else:
            prescale = ((25000000.0 / freq)/4096) -1
        
        #PRESCALE Reg unlock
        data = self.read_reg(self._REG_PCA9685_MODE1)
        self.write_reg(self._REG_PCA9685_MODE1,data|self._MODE1_SLEEP_LOWPOWER)
        self.write_reg(self._REG_PCA9685_PRESCALE,prescale)
        self.write_reg(self._REG_PCA9685_MODE1,data)
        
    def setPwmDuty(self,pwmch,duty_cnt):
        dely_time = 0
        self.write_regs(self._REG_PCA9685_LED0_ON_L+4*pwmch, 
                [dely_time & 0xFF,(dely_time >>8), duty_cnt & 0xFF,(duty_cnt >>8)])
        data = self.getPwmDuty(pwmch)
    def getPwmDuty(self,pwmch):
        dely_time = 0
        on_l = self.read_reg(self._REG_PCA9685_LED0_ON_L+4*pwmch)
        on_h = self.read_reg(self._REG_PCA9685_LED0_ON_H+4*pwmch)
        off_l = self.read_reg(self._REG_PCA9685_LED0_OFF_L+4*pwmch)
        off_h = self.read_reg(self._REG_PCA9685_LED0_OFF_H+4*pwmch)
        duty_cnt = (0x0FFF& (off_l | off_h <<8)-(0x0FFF&(on_l|on_h<<8 )))   
        return duty_cnt
    def cleanup(self):
        self.extbus.close()
