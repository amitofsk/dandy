#This class displays a numeric value, such as from an analog input sensor,
# as a needle on a dial. It is a child of AnalogInDisplay.

import tkinter as tk
import math
import sys  
sys.path.append ('../widgets') 
import AnalogInDisplay as ain


class DialDisplay(ain.AnalogInDisplay):
    def __init__(self, windowDD, height=100, width=100):
        super().__init__(windowDD, a_height=height, a_width=width)
        self.__xOrigin=0.5*self.get_ain_width()
        self.__yOrigin=0.95*self.get_ain_height()
        #radius_scale_factor sets the fraction of the window used by the widget.
        self.__radius_scale_factor=0.9 
        if height<width:
            self.__radius=0.5*self.__radius_scale_factor*self.get_ain_height()
        else:
            self.__radius=0.5*self.__radius_scale_factor*self.get_ain_width()
        self.__xStart=self.__xOrigin-self.__radius
        self.__xStop=self.__xOrigin+self.__radius
        self.__yStart=self.__yOrigin-self.__radius
        self.__yStop=self.__yOrigin+self.__radius
        self.__dial_top=self.ain_canvas.create_arc(self.__xStart, self.__yStart, \
                             self.__xStop, self.__yStop, start=0, extent=180, \
                            fill=self.get_color1(), style="pieslice")
        self.__lineA=self.ain_canvas.create_line(self.__xStart, self.__yOrigin, \
                            self.__xOrigin, self.__yOrigin, width=2 )
        windowDD.update()


    def set_to_value(self, aValue):
        self.ain_canvas.delete(self.__lineA)
        self.ain_canvas.delete(self.__dial_top)
        xpos=self.__xOrigin-self.__radius*math.cos(math.pi*aValue \
                                    /(self.get_maximum()-self.get_minimum()))
        ypos=self.__yOrigin-self.__radius*math.sin(math.pi*aValue \
                                    /(self.get_maximum()-self.get_minimum()))
        self.__lineA=self.ain_canvas.create_line(xpos, ypos, self.__xOrigin, \
                                    self.__yOrigin, width=2 )
        dial_angle=(math.atan((self.__yOrigin-ypos)/(xpos-self.__xOrigin))*\
                            (180/math.pi))
        if(aValue>(0.5*self.get_maximum())):
           dial_angle=180-dial_angle
        else:
            dial_angle=-dial_angle
        self.__dial_top=self.ain_canvas.create_arc(self.__xOrigin-self.__radius, \
                            self.__yOrigin-self.__radius, \
                            self.__xOrigin+self.__radius, \
                            self.__yOrigin+self.__radius, \
                            start=180, extent=-dial_angle, \
                            fill=self.get_color1(), style="pieslice")
       

if __name__=="__main__":
    dial_example=tk.Tk()
    dial_widget=DialDisplay(dial_example, height=100, width=100)
    dial_widget.pack()
        
