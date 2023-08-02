#This class displays an analog input as if it were sent through a comparator
#to a tricolor LED. It relies on LEDDisplay.
#It is a child of LEDDisplay, not AnalogInDisplay... Not sure if this is right.

import tkinter as tk
import sys   
sys.path.append ('../widgets')  
import LEDDisplay as LEDD 

class TricolorDisplay(LEDD.LEDDisplay):
    def __init__(self, windowT, height=100, width=100, low_level=3.0, \
                 high_level=8.0):
        super().__init__(windowT, height=height, width=width)
        #self.triLED1=LEDDisplay.LEDDisplay(windowT)
        self.low_cutoff=low_level
        self.high_cutoff=high_level
        #self.triLED1.pack()
        windowT.update()

    def set_to_value(self, valueA):
        if valueA<self.low_cutoff:
            self.change_LED_color("green")
        elif valueA>self.high_cutoff:
            self.change_LED_color("red")
        else:
            self.change_LED_color("yellow")


    #Setter for cutoffs needed...
            


if __name__=="__main__":
    tricolor_example=tk.Tk()
    tricolor_widget=TricolorDisplay(tricolor_example)
    tricolor_widget.set_to_value(16.4)
    tricolor_widget.pack()
    



