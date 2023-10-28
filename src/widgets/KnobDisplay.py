#KnobDisplay displays a widget shaped like a knob. When you click with the left
#mouse button, the knob turns counter clockwise, and when you click with the
#right button, the knob turns clockwise. 

#References on tkinter bind:
#https://python-course.eu/tkinter/events-and-binds-in-tkinter.php
#https://stackoverflow.com/questions/23965767/key-binding-does-not-work-in-tkinter

#I wanted to set this up so that as you scrolled with the middle mouse button
#up or down, the knob would turn counter clockwise or clockwise. The
#instructions for this are below and commented out. They work fine under Linux
#but don't work under Windows. For that reason, this widget uses mouse clicks instead.

import tkinter as tk
import math

##TODO: Scale dot width to height? 

class KnobDisplay():
    def __init__(self, windowK, height=100, width=100):
        
        self.__height=height
        self.__width=width
        self.__color1='#007DC8'
        self.__color2='#98D2D2'
        self.__canvasK=tk.Canvas(windowK, height=height, width=width)
        self.__border=self.__canvasK.create_oval(0.1*width, 0.1*height, \
                        0.9*width, 0.9*height, outline=self.__color1, \
                        width=3, fill=self.__color2)
        self.__dot=self.__canvasK.create_oval(0.45*width, 0.20*height, \
                        0.55*width, 0.30*height, outline=self.__color1, width=3) 
        self.__angle=0
        self.__canvasK.pack()
        #self.__canvasK.focus_set()
        
        self.__canvasK.bind('<Button-3>', self.turn_clockwise)
        self.__canvasK.bind('<Button-1>', self.turn_counterwise)
        #If you want the knob to respond to scrolling the middle mouse wheel,
        #replace the two lines above with the two below. However,
        #these lines only work on Linux, not Windows. I'm not sure why.
        #self.__canvasK.bind('<Button-4>', self.turn_clockwise)
        #self.__canvasK.bind('<Button-5>', self.turn_counterwise)
         
       

    def pack(self):
        self.__canvasK.pack()


    def pack_forget(self):
        self.__canvasK.pack_forget()


    def get_angle(self):
        return self.__angle


    def turn_clockwise(self, event):
        self.__canvasK.delete(self.__dot)
        self.__angle=self.__angle+0.1
        centerX=0.5*self.__width+(0.25*self.__width*math.sin(self.__angle))
        centerY=0.5*self.__height-(0.25*self.__height*math.cos(self.__angle))
        self.__dot=self.__canvasK.create_oval((centerX-0.05*self.__width), \
                    (centerY-0.05*self.__height), (centerX+0.05*self.__width), \
                    (centerY+0.05*self.__height), outline=self.__color1, width=3)
        return self.__angle


    def turn_counterwise(self,event):
        self.__canvasK.delete(self.__dot)
        self.__angle=self.__angle-0.1
        centerX=0.5*self.__width+(0.25*self.__width*math.sin(self.__angle))
        centerY=0.5*self.__height-(0.25*self.__height*math.cos(self.__angle))
        self.__dot=self.__canvasK.create_oval((centerX-0.05*self.__width), \
                    (centerY-0.05*self.__height), (centerX+0.05*self.__width), \
                    (centerY+0.05*self.__height), outline=self.__color1, width=3)
        return self.__angle

if __name__=="__main__":
    example=tk.Tk()
    example_widget=KnobDisplay(example)
    example_widget.pack()
    tk.mainloop()
