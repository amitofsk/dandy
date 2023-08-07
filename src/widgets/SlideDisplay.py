#This class displays an analog input value as a slider.
#It is a child of AnalogInDisplay

import tkinter as tk
import sys  
sys.path.append ('../widgets')  
import AnalogInDisplay as ain

COLOR1='#007DC8'
COLOR2='#4B0000'
COLOR3='#98D2D2'

#These parameters set the fraction of the window used by the widget.
xScaleFactor=0.75
yScaleFactor=0.9


class SlideDisplay(ain.AnalogInDisplay):
    def __init__(self, windowS, height=100, width=100):
        super().__init__(windowS, a_height=height, a_width=width)
        self.__xLeft=(1-xScaleFactor)*self.get_ain_width()
        self.__xRight=xScaleFactor*self.get_ain_width()
        self.__yTop=(1-yScaleFactor)*self.get_ain_height()
        self.__yBottom=yScaleFactor*self.get_ain_height()
        self.__slide_border=self.ain_canvas.create_rectangle(self.__xLeft, \
                        self.__yTop, self.__xRight, self.__yBottom )
        self.__slide_fill=self.ain_canvas.create_rectangle(self.__xLeft, \
                        self.__yTop+20, self.__xRight, self.__yBottom, \
                        fill=COLOR1)
        windowS.update()

   
    def set_to_value(self, aValue):
        self.ain_canvas.delete(self.__slide_fill)
        hval=((1-yScaleFactor)-(self.__yBottom/self.get_maximum()))*aValue \
                    +self.__yBottom
        self.__slide_fill=self.ain_canvas.create_rectangle(self.__xLeft, hval, \
                    self.__xRight,self.__yBottom, fill=COLOR1)
               
    

if __name__=="__main__":
    slide_example=tk.Tk()
    slide_widget=SlideDisplay(slide_example)
    slide_widget.pack()
            
