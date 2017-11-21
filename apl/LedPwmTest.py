# -*- coding: utf-8 -*-

import sys
sys.path.append('../lib/base')
sys.path.append('../gui')
sys.path.append('../lib/hardware/extbus')
sys.path.append('../lib/hardware/device')
# GPIO Lib
import RPi.GPIO as GPIO
from led import Led
from ledpwm import LedPwm 
from sw import Sw
from guiled import GUILed
# TIME Lib
import time
# GUI Lib
import Tkinter as tk

class TestCtrl():
    def __init__(self):
        #Pin Num assain -> Connect assain
        GPIO.setmode(GPIO.BOARD)
        #create GUI  
        root = tk.Tk()
        root.title('LED & Switch')
        label = tk.Label(root,text='Led Test')
        label.pack()
        self.gui = GUILed(master=root)
        self.gui.createCircle(50,50,150,150,'black')
        self.gui.createSlidebar(callback=self.callback_changeDuty,fromval=0,toval=100)
        #create  instances
        self.gui.createButton(btn_name='Led',callback = self.callback_BtnLed)
        self.gui.createButton(btn_name='Finish',callback = self.cleanup)
        self.Sw = Sw(pin_no=7)
        #self.LedPwm = LedPwm(pin_no=11)
        self.Led = Led(11)
        GPIO.add_event_detect(self.Sw.getPinNo(),GPIO.BOTH,callback=self.callback_detectSwLed)
        # display GUI
        root.mainloop()
        self.cleanup()
    #  Flashing LED Test No.1
    def callback_BtnLed(self):
        if self.Led.getLedState() == 'Off':
            print 'Led on '
            self.gui.setColor('red') 
            #self.Ledpwm.setDuty(duty_val=100)
            self.Led.setLed('On')
        else:
            print 'Led Off'
            self.gui.setColor('black') 
            #self.LedPwm.setDuty(duty_val=0)
            self.Led.setLed('Off')
    def callback_detectSwLed(self,channel):
        self.SwState = self.Sw.getSwState()
        if self.SwState == 'Pressed':
            print 'SW is pressed.'
            #self.Led.setLed('On')
            #self.LedPwm.setDuty(duty_val=100)
            self.gui.setColor('red') 
        else:
            print 'SW is released'
            #self.Led.setLed('Off')
            #self.LedPwm.setDuty(duty_val=0)
            self.gui.setColor('black')
    def callback_changeDuty(self,dc):
        #self.LedPwm.setDuty(self.gui.getSlidebarLv())
        if self.gui.getSlidebarLv() == 0:
            self.gui.setColor('black')
        else:
            self.gui.setColor('red')
        
    def cleanup(self):
        print 'Test Finished'
        try:
            #self.LedPwm.stop()
            self.Led.cleanup()
        except RuntimeWarning:
            pass
        sys.exit()

if __name__ == '__main__':
    print "LED"
    App = TestCtrl()
    pass
        
    
        
