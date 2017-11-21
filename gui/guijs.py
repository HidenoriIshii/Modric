# -*- coding: utf-8 -*-
# GUI Lib
from Tkinter import *
import Tkinter as tk

class GuiJs(tk.Frame):
    def __init__(self, master=None):
        self.master = master
        tk.Frame.__init__(self,master)
        self.Canvas = tk.Canvas(self.master,width=500,height=500)
        #set Canvas 
        self.Canvas.pack()
    def createCircle(self,x_start,y_start,x_end,y_end,init_color):
        # set Circle in Capynvas
        self.Circle = self.Canvas.create_oval(x_start,y_start,x_end,y_end,fill=init_color)
    def createButton(self,btn_name='',callback=None):
         if callback != None:
            #set Finish Button
            button = tk.Button(self.master,text=btn_name,command=callback)
            button.pack()
    def createCordinateLabel(self):
        self.varCordinate = StringVar()
        self.LabelCordinate = Label(self.master,textvariable=self.varCordinate,relief=RAISED)
        self.varCordinate.set('Vert:0,Horz:0')
        self.LabelCordinate.pack()
    def moveCircle(self,x,y):
        self.Canvas.move(self.Circle,x,y)
    def setColor(self,color):
        self.Canvas.itemconfig(self.Circle,fill=color)
    def renewCordinate(self,vert,horz):
        self.varCordinate.set('Vert:%d'% vert + 'Horz:%d'% horz)
