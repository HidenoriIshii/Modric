# -*- coding: utf-8 -*-

import sys
sys.path.append('../lib/base')
sys.path.append('../gui')
sys.path.append('../lib/hardware/extbus')
sys.path.append('../lib/hardware/device')
from servmotor import ServMotor
from joystick import JoyStick
from guijs    import GuiJs
from led      import Led
from sw       import Sw
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
        self.gui.createCordinateLabel()
        self.gui.createCircle(200,200,220,220,'red')
        self.gui.createButton(btn_name='Finish',callback=self.cleanup)
        #JoyStick instanse
        self.js = JoyStick()
        self.val_vert = 0
        self.val_horz = 0
        self.move_vert = 0
        self.move_horz = 0
        #ServMotor
        self.sm= ServMotor(18,180,0)
        # Led instance
        self.Led = Led(17)
        self.Sw = Sw(4,'either',self.callback_Sw)
        #display GUI
    def cleanup(self):
        print 'Test Finished'
        self.js.cleanup()
        self.sm.cleanup()
        self.Led.cleanup()
        sys.exit()
    #  Flashing LED Test No.1
    def callback_Sw(self):
        if self.Sw.getState()== 'Released':
            if self.Led.getState() != 'Off':self.Led.setLedOff()
        else:
            if self.Led.getState() != 'On':self.Led.setLedOn()

    def test(self):
        self.val_vert = self.js.getValVert()
        self.val_horz = self.js.getValHorz()
        self.move_vert = self.movement(self.val_vert)
        self.move_horz = self.movement(self.val_horz)
        #:print (self.val_vert,self.val_horz,self.move_vert,self.move_horz)
        if self.move_vert == 0 and self.move_horz == 0:
            self.Led.setLedOff()
        else:self.Led.setLedOn()
        self.gui.renewCordinate(self.val_vert,self.val_horz)
        self.gui.moveCircle(self.move_vert,self.move_horz)
        self.moveServmoter()
        self.master.after(50,self.test)
    def movement(self,val):
        move_val = 0
        if val > 255:move_val = -10
        elif val > 63:move_val = -5
        elif val <= -512:move_val = 0 
        elif val < -255:move_val = 10
        elif val < -63: move_val = 5
        return move_val
    def moveServmoter(self):
        deg = self.sm.getDeg()
        if self.val_horz > 100:
            if deg  < 180:
                deg += 10
                print deg
                self.sm.setDeg(float(deg))
        elif self.val_horz < -200:
            if deg >= 10:
                deg -= 10
                print deg
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
