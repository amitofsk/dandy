#This class displays an analog input value as a slider.
#It is a child of AnalogInDisplay

import tkinter as tk
import AnalogInDisplay as ain

xScaleFactor=0.75
yScaleFactor=0.9

class SlideDisplay(ain.AnalogInDisplay):
    def __init__(self, sdWindow):
        super().__init__(sdWindow)
        self.xLeft=(1-xScaleFactor)*self.aInWidth
        self.xRight=xScaleFactor*self.aInWidth
        self.yTop=(1-yScaleFactor)*self.aInHeight
        self.yBottom=yScaleFactor*self.aInHeight
        self.slideBorder=self.aInCanvas.create_rectangle(self.xLeft, self.yTop, self.xRight, self.yBottom)
        self.slideFill=self.aInCanvas.create_rectangle(self.xLeft, self.yTop+20, self.xRight, self.yBottom, fill="pink")
        sdWindow.update()

    #New constructor scalable to different sizes?


    def setToValue(self, aValue):
        self.aInCanvas.delete(self.slideFill)
        hval=-8*aValue+self.yBottom
        self.slideFill=self.aInCanvas.create_rectangle(self.xLeft,hval,self.xRight,self.yBottom, fill='pink')
        #I don't think I need an update here, but I'm not sure.        
       


if __name__=="__main__":
    slideWidget=tk.Tk()
    slideWidg=SlideDisplay(slideWidget)
    slideWidg.pack()
            
