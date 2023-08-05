#This class displays an analog input value as a needle on a dial.
#It is a child of AnalogInDisplay.

import tkinter as tk
import math
import sys  
sys.path.append ('../widgets') 
import AnalogInDisplay as ain  

#This factor sets the fraction of the window used by the display
radiusScaleFactor=0.9

class DialDisplay(ain.AnalogInDisplay):
    def __init__(self, windowDD, height=100, width=100):
        super().__init__(windowDD, a_height=height, a_width=width)
        self.__xOrigin=0.5*self.get_ain_width()
        self.__yOrigin=0.95*self.get_ain_height()
        if height<width:
            self.__radius=0.5*radiusScaleFactor*self.get_ain_height()
        else:
            self.__radius=0.5*radiusScaleFactor*self.get_ain_width()
        
        self.__xStart=self.__xOrigin-self.__radius
        self.__xStop=self.__xOrigin+self.__radius
        self.__yStart=self.__yOrigin-self.__radius
        self.__yStop=self.__yOrigin+self.__radius
        self.__dial_top=self.ain_canvas.create_arc(self.__xStart, self.__yStart, \
                            self.__xStop, self.__yStop, start=0, extent=180, \
                            fill="blue", style="pieslice")
        self.__lineA=self.ain_canvas.create_line(self.__xStart, self.__yOrigin, \
                            self.__xOrigin, self.__yOrigin, width=2)
        windowDD.update()



    def set_to_value(self, aValue):
        self.ain_canvas.delete(self.__lineA)
 #       self.__dial_top=self.ain_canvas.create_arc(self.__xStart, self.__yStart, \
 #                           self.__xStop, self.__yStop, start=0, extent=180, \
 #                           fill="gray", style="pieslice")
        xpos=self.__xOrigin-self.__radius*math.cos(math.pi*aValue \
                                    /(self.get_maximum()-self.get_minimum()))
        ypos=self.__yOrigin-self.__radius*math.sin(math.pi*aValue \
                                    /(self.get_maximum()-self.get_minimum()))
        self.__lineA=self.ain_canvas.create_line(xpos, ypos, self.__xOrigin, \
                                    self.__yOrigin, width=2)
  #      dial_angle=math.atan((ypos-self.__yStart)/(self.__xStart-xpos))*\
  #                          (180/math.pi) 
   #     self.__dial_top=self.ain_canvas.create_arc(self.__xStart, self.__yStart, \
  #                          xpos, ypos, start=0, extent=180, \
   #                         fill="blue", style="pieslice")
       
        #To do here... Change it so that you only fill color to the needle?


if __name__=="__main__":
    dial_example=tk.Tk()
    dial_widget=DialDisplay(dial_example)
    dial_widget.pack()
        
