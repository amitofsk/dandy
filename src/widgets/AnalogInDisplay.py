#This is a parent class of widgets used for displaying analog input.
#The child classes are SlideDisplay, SimplePlotDisplay, DialDisplay,
#and TricolorDisplay. You should probably use the child classes instead.

import tkinter as tk

class AnalogInDisplay:
    #Here's the constructor for when you don't have any options
    def __init__(self, windowAIn, a_height=100, a_width=100):
        self.__minimum=0.0
        self.__maximum=10.0
        self.__ain_height=a_height
        self.__ain_width=a_width
        self.ain_canvas=tk.Canvas(windowAIn, height=self.__ain_height, \
                                 width=self.__ain_width)

    ##Setters and getters
    def set_minimum(self, min_value=0):
        self.__minimum=min_value


    def set_maximum(self, max_value=10.0):
        self.__maximum=max_value


    def get_minimum(self):
        return self.__minimum


    def get_maximum(self):
        return self.__maximum


    def set_ain_height(self, aheight=100):
        self.__ain_height=aheight


    def set_ain_width(self, awidth=100):
        self.__ain_width=awidth


    def get_ain_height(self):
        return self.__ain_height


    def get_ain_width(self):
        return self.__ain_width
        

    ##Member functions related to packing
    def pack(self):
        self.ain_canvas.pack()


    def pack_forget(self):
        self.ain_canvas.pack_forget()



#When you run main, you should get a blank window. This class is really supposed to be
#abstract. You really should only use its children.
if __name__=="__main__":
    analog_in_example=tk.Tk()
    analog_in_widget=AnalogInDisplay(analog_in_example)
    analog_in_widget.pack()
