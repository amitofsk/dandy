#This class displays an analog input value as a slider.
#It is a child of AnalogInDisplay

import tkinter as tk
import sys  
sys.path.append ('../widgets')  
import AnalogInDisplay as ain 

xScaleFactor=0.75
yScaleFactor=0.9

class SlideDisplay(ain.AnalogInDisplay):
    def __init__(self, windowS, height=100, width=100):
        super().__init__(windowS, a_height=height, a_width=width)
        self.xLeft=(1-xScaleFactor)*self.ain_width
        self.xRight=xScaleFactor*self.ain_width
        self.yTop=(1-yScaleFactor)*self.ain_height
        self.yBottom=yScaleFactor*self.ain_height
        self.slide_border=self.ain_canvas.create_rectangle(self.xLeft, \
                        self.yTop, self.xRight, self.yBottom)
        self.slide_fill=self.ain_canvas.create_rectangle(self.xLeft, \
                        self.yTop+20, self.xRight, self.yBottom, fill="pink")
        windowS.update()

   
    def set_to_value(self, aValue):
        self.ain_canvas.delete(self.slide_fill)
        hval=((1-yScaleFactor)-(self.yBottom/self.maximum))*aValue \
                    +self.yBottom
        self.slide_fill=self.ain_canvas.create_rectangle(self.xLeft, hval, \
                    self.xRight,self.yBottom, fill='pink')
        #I don't think I need an update here, but I'm not sure.        
    

if __name__=="__main__":
    slide_example=tk.Tk()
    slide_widget=SlideDisplay(slide_example)
    slide_widget.pack()
            
