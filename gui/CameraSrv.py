# -*- coding: utf-8 -*-
# Camera Lib
import  picamera
# GUI Lib
import Tkinter as tk

class CameraSrv():
    def __init__(self):
        # Camera Default Setting
        self.WB = 'auto'
        self.Contrast = 50
        # ISO auto
        self.ISO = 0
        self.Brightness = 0
        self.ExposureMode = 'auto'
        self.ImageEffect = 'none'
        # Resolution = 640x480
        self.Resolution = 2
        self.Saturation = 0
        # Shutter Speed Auto
        self.Shutter_speed = 0
        # Sharpness Auto
        self.Sharpness = 0
        self.Rotation = 0        
