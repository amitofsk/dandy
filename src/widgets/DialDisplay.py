#This class displays an analog input value as a needle on a dial.
#It is a child of AnalogInDisplay.

import tkinter as tk
import math
import AnalogInDisplay as ain

radiusScaleFactor=0.9

class DialDisplay(ain.AnalogInDisplay):
    def __init__(self, ddWindow):
        super().__init__(ddWindow)
        self.xOrigin=0.5*self.aInWidth
        self.yOrigin=0.75*self.aInHeight
        self.radius=radiusScaleFactor*self.xOrigin
        self.xStart=self.xOrigin-self.radius
        self.xStop=self.xOrigin+self.radius
        self.yStart=self.yOrigin-self.radius
        self.yStop=self.yOrigin+self.radius
        self.dialTop=self.aInCanvas.create_arc(self.xStart,self.yStart,self.xStop,self.yStop, start=0, extent=180, \
                                               fill="pink", style="pieslice")
        self.lineA=self.aInCanvas.create_line(self.xStart,self.yOrigin,self.xOrigin,self.yOrigin, width=2)
        ddWindow.update()


    #New constructor scalable to different sizes?


    def setToValue(self, aValue):
        self.aInCanvas.delete(self.lineA)
        xpos=self.xOrigin-self.radius*math.cos(math.pi*aValue/(self.maximum-self.minimum))
        ypos=self.yOrigin-self.radius*math.sin(math.pi*aValue/(self.maximum-self.minimum))
        self.lineA=self.aInCanvas.create_line(xpos, ypos, self.xOrigin, self.yOrigin, width=2)
        #I don't think I need an update here, but I'm not sure.  
        #To do here... Change it so that you only fill color to the needle?



        
if __name__=="__main__":
    dialWidget=tk.Tk()
    dialWidget.aInValue=5.2
    dialWidg=DialDisplay(dialWidget)
    dialWidg.pack()
        
