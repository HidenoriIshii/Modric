# -*- coding: utf-8 -*-
# GUI Lib
import Tkinter as tk

class GUILed(tk.Frame):
    def __init__(self, master=None):
        self.master = master
        tk.Frame.__init__(self,master)
        self.Canvas = tk.Canvas(self.master,width=300,height=200)
        #set Canvas 
        self.Canvas.pack()
    def createCircle(self,x_start,y_start,x_end,y_end,init_color):
        # set Circle in Canvas
        self.Circle = self.Canvas.create_oval(x_start,y_start,x_end,y_end,fill=init_color)
    def createButton(self,btn_name='',callback=None):
         if callback != None:
            #set Finish Button
            button = tk.Button(self.master,text=btn_name,command=callback)
            button.pack()
    def createSlidebar(self,callback=None,fromval=0,toval=0):
         if callback != None:
             self.slideValue= tk.DoubleVar()
             slidebar = tk.Scale(self.master,orient='h',from_ = fromval,to = toval,\
                            variable = self.slideValue,command=callback)
             slidebar.pack()

    def getSlidebarLv(self):
        return self.slideValue.get()
    
    def setColor(self,color):
        self.Canvas.itemconfig(self.Circle,fill=color)
