# -*- coding: utf-8 -*-
import os
import sys
sys.path.append('/home/pi/python_apl')
sys.path.append('/home/pi/python_apl/lib/base')
sys.path.append('/home/pi/python_apl/gui')
sys.path.append('/home/pi/python_apl/lib/hardware/extbus')
sys.path.append('/home/pi/python_apl/lib/hardware/device')
#from pwmservo import PwmServo
from i2cservo import I2cServo
from joystick import JoyStick
from guirobotarm    import GuiRarm
from led      import Led
from sw		import Sw
from volume import Volume
# TIMER Lib
import time
#GUI Lib
import Tkinter as tk
import pigpio

class RobotArmTest(tk.Frame):
    def __init__(self,master):
        # create GUI
        self.gpio = pigpio.pi()
        self.master = master
        self.master.title('JoyStick Test')
        label = tk.Label(root,text='Joystick')
        label.pack()
        self.gui = GuiRarm(master=root)
        self.gui.createCordinateLabelServo()
        self.gui.createButton(btn_name='Finish',callback=self.cleanup)
        #self.gui.createCircleJs2(200,200,220,220,'blue')
        #JoyStick instanse
        self.jsR = JoyStick(-1,4,27)
        self.val_horz = 0
        #self.jsL = JoyStick(7,4,22)
        self.jsL = JoyStick(2,-1,22)
        self.val_vert = 0
        #Volume instance
	self.vol = Volume(6)
	self.val_vol = 0
	self.vol_sum = 0
	self.sampleCount = 0
	#ServMotor
        #self.servo= ServMotor(18,180,0)
        self.servo = I2cServo()
        #PWM Freq: 60Hz
        self.servo.setPWMFreq(60)
        # Led instance
        self.Led = Led(4)
        self.Led.setLedOn()
	# PowrSw
	self.PowSw = Sw(17,pud='pudup')
	self.PowSwCont = 0
        #display GUI
    def shutdown(self):
        self.Led.setLedOff()
        self.jsR.cleanup()
        self.jsL.cleanup()
        self.vol.cleanup()
        self.servo.cleanup()
        self.Led.cleanup()
        # release pigpio resources
        self.gpio.stop()
	os.system("sudo shutdown -h now")
    def cleanup(self):
        print ('Test Finished')
        self.Led.setLedOff()
        self.jsR.cleanup()
        self.jsL.cleanup()
        self.vol.cleanup()
	self.servo.cleanup()
        self.Led.cleanup()
        # release pigpio resources
        self.gpio.stop()
        sys.exit()
    #  Flashing LED Test No.1
    def test(self):
	if self.PowSw.getState() == 'Pressed':
	    self.PowSwCont += 1
	    if self.PowSwCont == 10:
	        print 'Pressed'
		print 'Shutdown!'
		self.shutdown()
	else:
	    self.PowSwCont = 0
	    
        self.val_horz = self.jsR.getValHorz()
        self.val_vol = self.vol.getValVol()/4
        self.val_vert = self.jsL.getValVert()
        self.moveI2cServoHorz()
        self.moveI2cServoVert()
        self.moveI2cServoVol()
        self.gui.renewCordinateServo(self.duty_horz,self.duty_vert,self.val_vol)
	#call self.test() per 6msec 
        self.master.after(6,self.test)
    def moveI2cServoHorz(self):
        self.duty_horz = self.servo.getDuty(self.servo._I2CSERVO_HORZ_0)
#        print ('horzduty :%d' %duty)
        # turn to -90
        if self.val_horz  >= 2: self.duty_horz += 5
        # turn to 90
        elif self.val_horz <= 0: self.duty_horz -= 5
        # dont turn
        else :return 
        self.servo.setDuty(self.servo._I2CSERVO_HORZ_0,self.duty_horz)
    def moveI2cServoVert(self):
        self.duty_vert = self.servo.getDuty(self.servo._I2CSERVO_VERT_0)
 #       print ('vertduty :%d' %duty)
        # turn to -90
        if self.val_vert  >= 2: self.duty_vert -= 5
        # turn to 90
        elif self.val_vert <= 0: self.duty_vert += 5
        # dont turn
        else :return 
        self.servo.setDuty(self.servo._I2CSERVO_VERT_0,self.duty_vert)
    def moveI2cServoVol(self):
        if self.sampleCount < 5:
	   self.vol_sum += self.val_vol
	   self.sampleCount +=1
	else:
	   val = self.vol_sum / 5  
	   self.servo.setAdValtoDuty(self.servo._I2CSERVO_VOL_0,val,0,255)
           self.sampleCount = 0
	   self.vol_sum = 0
if __name__ == '__main__':
    root = tk.Tk()
    App = RobotArmTest(root)
    try:
        App.test()
        root.mainloop()
    except KeyboardInterrupt:
       pass
    App.cleanup()
    pass
