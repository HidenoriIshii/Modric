# -*- coding: utf-8 -*-
# GUI Lib
from Tkinter import *
import Tkinter as tk

class GuiRarm(tk.Frame):
    def __init__(self, master=None):
        self.master = master
        tk.Frame.__init__(self,master)
        self.CanvasServo = tk.Canvas(self.master,width=500,height=500)
        #set CanvasServo 
        self.CanvasServo.pack()
    def createCircleJs1(self,x_start,y_start,x_end,y_end,init_color): 
        # set Circle in Capynvas
        self.CircleJs1 = self.CanvasServo.create_oval(x_start,y_start,x_end,y_end,fill=init_color)
    def createCircleJs2(self,x_start,y_start,x_end,y_end,init_color): 
        # set Circle in Capynvas
        self.CircleJs2 = self.CanvasServo.create_oval(x_start,y_start,x_end,y_end,fill=init_color)
    def createButton(self,btn_name='',callback=None):
         if callback != None:
            #set Finish Button
            button = tk.Button(self.master,text=btn_name,command=callback)
            button.pack()
    def createCordinateLabelServo(self):
        self.varCordinateServo = StringVar()
        self.LabelCordinateServo = Label(self.master,textvariable=self.varCordinateServo,relief=RAISED)
        self.varCordinateServo.set('Servo Vert:0,Horz:0,Volume:0 ')
        self.LabelCordinateServo.pack()
    def moveCircle1(self,x,y):
        self.CanvasServo.move(self.CircleJs1,x,y)
    def moveCircle2(self,x,y):
        self.CanvasServo.move(self.CircleJs2,x,y)
    def setColor(self,color):
        self.CanvasServo.itemconfig(self.Circle,fill=color)
    def renewCordinateServo(self,vert,horz,volume ):
        self.varCordinateServo.set('Servo'+ 'Vert:%d'% vert + 'Horz:%d'% horz +'Volume:%d' % volume )
