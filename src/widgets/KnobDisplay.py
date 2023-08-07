#KnobDisplay displays a widget shaped like a knob. When you scroll with the
#middle mouse button, self.__angle changes.

#Reference on tkinter bind:
#https://python-course.eu/tkinter/events-and-binds-in-tkinter.php
import tkinter as tk
import math


COLOR1='#007DC8'
COLOR2='#4B0000'
COLOR3='#98D2D2'

class KnobDisplay():
    def __init__(self, windowK, height=100, width=100):
        
        self.__height=height
        self.__width=width
        self.__canvasK=tk.Canvas(windowK, height=height, width=width)
        self.__border=self.__canvasK.create_oval(0.1*width, 0.1*height, \
                        0.9*width, 0.9*height, outline=COLOR1, width=3,\
                        fill=COLOR3)
        self.__dot=self.__canvasK.create_oval(0.45*width, 0.20*height, \
                        0.55*width, 0.30*height, outline=COLOR1, width=3) 
        self.__angle=0
        self.__canvasK.pack()
        self.__canvasK.bind('<Button-4>', self.turn_clockwise)
        self.__canvasK.bind('<Button-5>', self.turn_counterwise)
       

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
                    (centerY+0.05*self.__height), outline=COLOR1, width=3)
        return self.__angle


    def turn_counterwise(self,event):
        self.__canvasK.delete(self.__dot)
        self.__angle=self.__angle-0.1
        centerX=0.5*self.__width+(0.25*self.__width*math.sin(self.__angle))
        centerY=0.5*self.__height-(0.25*self.__height*math.cos(self.__angle))
        self.__dot=self.__canvasK.create_oval((centerX-0.05*self.__width), \
                    (centerY-0.05*self.__height), (centerX+0.05*self.__width), \
                    (centerY+0.05*self.__height), outline=COLOR1, width=3)
        return self.__angle

if __name__=="__main__":
    example=tk.Tk()
    example_widget=KnobDisplay(example)
    example_widget.pack()
    tk.mainloop()
