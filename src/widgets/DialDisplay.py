#This class displays an analog input value as a needle on a dial.
#It is a child of AnalogInDisplay.

import tkinter as tk
import math
import sys  
sys.path.append ('../widgets') 
import AnalogInDisplay as ain  

radiusScaleFactor=0.9

class DialDisplay(ain.AnalogInDisplay):
    def __init__(self, windowDD, height=100, width=100):
        super().__init__(windowDD, a_height=height, a_width=width)
        self.xOrigin=0.5*self.ain_width
        self.yOrigin=0.95*self.ain_height
        if height<width:
            self.radius=0.5*radiusScaleFactor*self.ain_height
        else:
            self.radius=0.5*radiusScaleFactor*self.ain_width
        
        self.xStart=self.xOrigin-self.radius
        self.xStop=self.xOrigin+self.radius
        self.yStart=self.yOrigin-self.radius
        self.yStop=self.yOrigin+self.radius
        self.dial_top=self.ain_canvas.create_arc(self.xStart, self.yStart, \
                            self.xStop, self.yStop, start=0, extent=180, \
                            fill="pink", style="pieslice")
        self.lineA=self.ain_canvas.create_line(self.xStart, self.yOrigin, \
                            self.xOrigin, self.yOrigin, width=2)
        windowDD.update()



    def set_to_value(self, aValue):
        self.ain_canvas.delete(self.lineA)
        xpos=self.xOrigin-self.radius*math.cos(math.pi*aValue \
                                    /(self.maximum-self.minimum))
        ypos=self.yOrigin-self.radius*math.sin(math.pi*aValue \
                                    /(self.maximum-self.minimum))
        self.lineA=self.ain_canvas.create_line(xpos, ypos, self.xOrigin, \
                                    self.yOrigin, width=2)
        #I don't think I need an update here, but I'm not sure.  
        #To do here... Change it so that you only fill color to the needle?


if __name__=="__main__":
    dial_example=tk.Tk()
    dial_widget=DialDisplay(dial_example)
    dial_widget.pack()
        
