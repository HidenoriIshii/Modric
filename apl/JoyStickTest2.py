# -*- coding: utf-8 -*-

import sys
sys.path.append('../lib/base')
sys.path.append('../gui')
sys.path.append('../lib/hardware/extbus')
sys.path.append('../lib/hardware/device')
#from pwmservo import PwmServo
from i2cservo import I2cServo
from joystick import JoyStick
from guijs    import GuiJs
from led      import Led
# TIMER Lib
import time
#GUI Lib
import Tkinter as tk

class JoyStickTest(tk.Frame):
    def __init__(self,master):
        # create GUI
        self.master = master
        self.master.title('JoyStick Test')
        label = tk.Label(root,text='Joystick')
        label.pack()
        self.gui = GuiJs(master=root)
        self.gui.createCordinateLabelJs1()
        self.gui.createCordinateLabelJs2()
        self.gui.createCircleJs1(200,200,220,220,'red')
        self.gui.createButton(btn_name='Finish',callback=self.cleanup)
        self.gui.createCircleJs2(200,200,220,220,'blue')
        #JoyStick instanse
        self.js1 = JoyStick(0,3,27)
        self.val_vert1 = 0
        self.val_horz1 = 0
        self.move_vert1 = 0
        self.move_horz1 = 0
        self.js2 = JoyStick(7,4,22)
        self.val_vert2 = 0
        self.val_horz2 = 0
        self.move_vert2 = 0
        self.move_horz2 = 0
        #ServMotor
        #self.servo= ServMotor(18,180,0)
        #self.servo = I2cServo()
        # Led instance
        self.Led = Led(17)
        #display GUI
    def cleanup(self):
        print 'Test Finished'
        self.js1.cleanup()
        self.js2.cleanup()
        #self.servo.cleanup()
        self.Led.cleanup()
        sys.exit()
    #  Flashing LED Test No.1
    def setLed(self):
        if (self.js1.getSelState()== 'Released') and \
           (self.js2.getSelState()== 'Released'):
            if self.Led.getState() != 'Off':self.Led.setLedOff()
        else:
            if self.Led.getState() != 'On':self.Led.setLedOn()
    def test(self):
        self.val_vert1 = self.js1.getValVert()
        self.val_horz1 = self.js1.getValHorz()
        self.move_vert1 = self.move_vert(self.val_vert1)
        self.move_horz1 = self.move_horz(self.val_horz1)
        #print ('Js1'+'vert:%d'% self.val_vert1+'hortz:%d'% self.val_horz1+'sel:%d' % self.val_sel1)
        #print (self.val_vert1,self.val_horz1,self.move_vert1,self.move_horz1)
        self.val_vert2 = self.js2.getValVert()
        self.val_horz2 = self.js2.getValHorz()
        self.move_vert2 = self.move_vert(self.val_vert2)
        self.move_horz2 = self.move_horz(self.val_horz2)
        #print ('Js2'+'vert:%d'% self.val_vert2+'hortz:%d'% self.val_horz2+'sel:%d' % self.val_sel2)
#        if self.move_vert1 == 0 and self.move_horz1 == 0:
#            self.Led.setLedOff()
#        else:self.Led.setLedOn()
        self.gui.renewCordinateJs1(self.val_vert1,self.val_horz1)
        self.gui.renewCordinateJs2(self.val_vert2,self.val_horz2)
        self.gui.moveCircle1(self.move_horz1,self.move_vert1)
        self.gui.moveCircle2(self.move_horz2,self.move_vert2)
        #self.movePwmServo()
        #self.moveI2cServo()
        self.setLed()
        # check Adc(vert,Horz) and Sw per 50ms 
        self.master.after(30,self.test)
    def move_vert(self,val):
        move_val = 0
        if val >= 2:move_val = -10
        elif val <= 0:move_val = 10
        else :move_val = 0 
        return move_val
    def move_horz(self,val):
        move_val= 0
        if val >= 2:move_val = -10
        elif val <= 0:move_val = 10
        else :move_val = 0 
        return move_val
    def moveI2cServo(self):
        self.servo.setDuty(self.servo._I2CSERVO_HORZ_0,self.val_horz1,0,1024)
        self.servo.setDuty(self.servo._I2CSERVO_VERT_0,self.val_vert2,0,1024)
    def movePwmServo(self):
        deg = self.sm.getDeg()
        if self.val_horz1 > 100:
            if deg  < 180:
                deg += 10
                self.sm.setDeg(float(deg))
        elif self.val_horz1 < -200:
            if deg >= 10:
                deg -= 10
                self.sm.setDeg(float(deg))
if __name__ == '__main__':
    root = tk.Tk()
    App = JoyStickTest(root)
    try:
        App.test()
        root.mainloop()
    except KeyboardInterrupt:
       pass
    App.cleanup()
    pass
