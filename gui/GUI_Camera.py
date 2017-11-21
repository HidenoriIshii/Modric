# -*- coding: utf-8 -*-
# GUI Lib

import wx
class GUI_Camera():
    def __init__(self,master=None)
       frame
        #  Camera Setting Label Lists
        cam_wb= [('OFF',0),('Auto',1),('Sunlight',2),('Cloudy',3),('Shade',4),('Tungsten',5),\
                   ('Flourescent',6),('Incandescent',7),('Flash',8),('Horizon',9)]
        cam_iso = [('Auto',0),('100',1),('200',2),('320',3),('400',4),('500',5),('640',6),('800',7),('1600',8),]
        cam_resolution = [('320x240',1),('640x480',2),('1024x768',3),]
        cam_exposuremode = [('OFF,'0),('Auto,'1),('Night',2),('Nightpreview',3),('Backlight',4),\
                            ('Spotlight',5),('Sports',6),('Snow',7),('Beach',8),\
                            ('Verylong',9),('Fixedfps',10),('Antishake',11),('Fireworks',12)]
        cam_image_effect = [('None',0),('Negative',1),('Solarize',2),('Sketch',3),('Denoise',4),('Emboss',5),\
                             ('Oilpaint',6),('Hacth',7),('Gpen',8),('Pastel',9),('Watercolor',10),('Film',11),\
                             ('Blur',12),('Staturation',13),('Colorswap',14),('Washedout',15),('Posterise',16),/
                             ('Colorpoint',17),('Colorbalance',18),('Cartoon',19),('Deinterlace1',20),('Deinterlace2',21)]
        cam_shutter_speed = [('Auto',0),('1s',1),('1/2s',2),('1/4s',3),('1/8s',4),\
                             ('1/15s',5),('1/30s',6),('1/60s',7),('1/125s',8),('1/250s',6),('1/500s',6),\
                             ('1/1000s',7),('1/2000s',8)]
        cam_rotation = [('0',0),('90',1),('180',2),('270',3)]
        # Slide Bar(saturation,sharpness)
        

