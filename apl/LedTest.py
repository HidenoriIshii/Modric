# -*- coding: utf-8 -*-

import sys
sys.path.append('../lib/base')
sys.path.append('../gui')
sys.path.append('../lib/hardware/extbus')
sys.path.append('../lib/hardware/device')
# GPIO Lib
from led import Led
from sw import Sw
from guiled import GUILed
# TIME Lib
import time
# GUI Lib
import Tkinter as tk

class LedTestCtrl():
    def __init__(self,master = 0):
        #create GUI  
        self.master = master
        root.title('LED & Switch')
        label = tk.Label(root,text='Led Test')
        label.pack()
        self.gui = GUILed(master=root)
        self.gui.createCircle(50,50,150,150,'black')
        #create  instances
        self.gui.createButton(btn_name='Led',callback = self.callback_BtnLed)
        self.gui.createButton(btn_name='Finish',callback = self.cleanup)
        self.Sw = Sw(4,'either',self.callback_Sw)
        self.Led = Led(17)
        # display GUI
    #  Flashing LED Test No.1
    def callback_Sw(self):
        if self.Sw.getState()== 'Released':
            if self.Led.getState() != 'Off':self.Led.setLedOff()
        else:
            if self.Led.getState() != 'On':self.Led.setLedOn()
    def callback_BtnLed(self):
        if self.Led.getState() == 'Off':
            self.gui.setColor('red')
            self.Led.setLedOn()
        else:
            self.gui.setColor('black')
            self.Led.setLedOff()
    def cleanup(self):
        print 'Test Finished'
        try:
            self.Led.cleanup()
        except RuntimeWarning:
            pass
        sys.exit()

if __name__ == '__main__':
    print "LED"
    root = tk.Tk()
    App = LedTestCtrl(root)
    try:
       # App.Test()
        root.mainloop()
    except KeyboardInterrupt:
        pass
    App.cleanup()
    pass
        
