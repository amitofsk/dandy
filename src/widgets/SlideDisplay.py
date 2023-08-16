# This class displays a numeric value, such as from an analog input sensor,
# as a slider. It is a child of AnalogInDisplay.

import tkinter as tk
import sys  
sys.path.append ('../widgets')  
import AnalogInDisplay as ain



class SlideDisplay(ain.AnalogInDisplay):
    def __init__(self, windowS, height=100, width=100):
        super().__init__(windowS, a_height=height, a_width=width)
        #xScaleFactor and yScaleFactor set the fraction of the window used.
        self.__xScaleFactor=0.75
        self.__yScaleFactor=0.9
        self.__xLeft=(1-self.__xScaleFactor)*self.get_ain_width()
        self.__xRight=self.__xScaleFactor*self.get_ain_width()
        self.__yTop=(1-self.__yScaleFactor)*self.get_ain_height()
        self.__yBottom=self.__yScaleFactor*self.get_ain_height()
        self.__slide_border=self.ain_canvas.create_rectangle(self.__xLeft, \
                        self.__yTop, self.__xRight, self.__yBottom )
        self.__slide_fill=self.ain_canvas.create_rectangle(self.__xLeft, \
                        self.__yTop+20, self.__xRight, self.__yBottom, \
                        fill=self.get_color1())
        windowS.update()

   
    def set_to_value(self, aValue):
        if (aValue>self.get_minimum()) and (aValue<self.get_maximum()):
            self.ain_canvas.delete(self.__slide_fill)
            hval=((1-self.__yScaleFactor)-(self.__yBottom/self.get_maximum()))\
                  *aValue+self.__yBottom
            self.__slide_fill=self.ain_canvas.create_rectangle(self.__xLeft, hval, \
                    self.__xRight,self.__yBottom, fill=self.get_color1())
               
    

if __name__=="__main__":
    slide_example=tk.Tk()
    slide_widget=SlideDisplay(slide_example)
    slide_widget.pack()
            
