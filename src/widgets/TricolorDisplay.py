#This class displays an analog input as if it were sent through a comparator
#to a tricolor LED. It relies on LEDDisplay.
#It is a child of LEDDisplay, not AnalogInDisplay.

import tkinter as tk
import sys   
sys.path.append ('../widgets')  
import LEDDisplay as LEDD 

class TricolorDisplay(LEDD.LEDDisplay):
    def __init__(self, windowT, height=100, width=100, low_level=3.0, \
                 high_level=8.0):
        super().__init__(windowT, height=height, width=width)
        self.__low_cutoff=low_level
        self.__high_cutoff=high_level
        windowT.update()


    def set_to_value(self, valueA):
        if valueA<self.__low_cutoff:
            self.change_LED_color("green")
        elif valueA>self.__high_cutoff:
            self.change_LED_color("red")
        else:
            self.change_LED_color("yellow")


    def set_low_cutoff(self, low_level):
        self.__low_cutoff=low_level


    def get_low_cutoff(self):
        return self.__low_cutoff


    def set_high_cutoff(self, high_level):
        self.__high_cutoff=high_level


    def get_high_cutoff(self):
        return self.__high_cutoff


if __name__=="__main__":
    tricolor_example=tk.Tk()
    tricolor_widget=TricolorDisplay(tricolor_example)
    tricolor_widget.set_to_value(16.4)
    tricolor_widget.pack()
    



