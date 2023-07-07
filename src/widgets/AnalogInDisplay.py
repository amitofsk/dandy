#This is a parent class of widgets used for displaying analog input.
#Should this be abstract?
#I recommend using the child classes instead.

import tkinter as tk

class AnalogInDisplay:
    #Here's the constructor for when you don't have any options
    def __init__(self, windowAIn, a_height=100, a_width=100):
        self.minimum=0.0
        self.maximum=10.0
        self.ain_height=a_height
        self.ain_width=a_width
        #self.ain_value=0.0
        self.ain_canvas=tk.Canvas(windowAIn, height=self.ain_height, \
                                 width=self.ain_width)


    #I'm writing the next function so that syntax is closer to syntax
    #of preexisting tkinter widgets. Yes, it seems a bit silly to have
    #such a short function, but there is a reason.
    def pack(self):
        self.ain_canvas.pack()    



#When you run main, you should get a blank window. This class is really supposed to be
#abstract. You really should only use its children.
if __name__=="__main__":
    analog_in_example=tk.Tk()
    analog_in_widget=AnalogInDisplay(analog_in_example)
    analog_in_widget.pack()
