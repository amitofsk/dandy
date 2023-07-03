#This class displays three analog inputs (x,y,z) as an vector.
#It is a child of AnalogInDisplay.

#Reference on Isometric Projection: https://en.wikipedia.org/wiki/Isometric_projection
#Let's start by assuming a viewing angle of theta=45 and phi=45. Later I can generalize this...

#Watch the minus signs carefully here, positive x is to the LEFT, (origin - newXValue).
#However, positive y is UP, so (origin-newYValue).
#I think I finally got the minus signs working here...


import tkinter as tk
import math #Is this needed?
import AnalogInDisplay as ain

radiusScaleFactor=0.75

class VectorDisplay(ain.AnalogInDisplay):
    def __init__(self, vdWindow):
        super().__init__(vdWindow)
        #xOrigin and yOrigin are used in Dial too. Maybe I should move them to AnalogInDisplay?
        self.xOrigin=0.5*self.aInWidth
        self.yOrigin=0.5*self.aInHeight
        self.radius=radiusScaleFactor*self.xOrigin
        self.thetaView=math.radians(45) 
        self.phiView=math.radians(225)
        self.xAxis=self.aInCanvas.create_line(self.xOrigin, self.yOrigin, (self.xOrigin-(math.cos(self.thetaView)*self.radius)), \
                                              (self.yOrigin-(math.sin(self.thetaView)*math.sin(self.phiView)*self.radius)), fill="blue", arrow=tk.LAST)
        self.yAxis=self.aInCanvas.create_line(self.xOrigin, self.yOrigin, self.xOrigin, (self.yOrigin-self.radius*math.cos(self.phiView)), fill="blue", arrow=tk.LAST)
        self.zAxis=self.aInCanvas.create_line(self.xOrigin,self.yOrigin ,(self.xOrigin-(-math.sin(self.thetaView)*self.radius)), \
                                              (self.yOrigin-(math.sin(self.phiView)*math.cos(self.thetaView)*self.radius)), fill="blue", arrow=tk.LAST)
        self.lineA=self.aInCanvas.create_line(self.xOrigin+self.radius , self.yOrigin+self.radius, self.xOrigin, self.yOrigin, width=2, arrow=tk.FIRST)
        vdWindow.update()

    #New constructor scalable to different sizes?

    def setToValue(self, xValue, yValue, zValue):
        xPos=0.0
        yPos=0.0
        self.aInCanvas.delete(self.lineA)
        xProjected=(xValue*math.cos(self.thetaView))-(zValue*math.sin(self.thetaView))
        yProjected=(xValue*math.sin(self.phiView)*math.sin(self.thetaView))+(yValue*math.cos(self.phiView))+ \
                    (zValue*math.sin(self.phiView)*math.cos(self.thetaView))
        xPos=self.xOrigin-xProjected
        yPos=self.yOrigin-yProjected 
        self.lineA=self.aInCanvas.create_line(xPos, yPos, self.xOrigin, self.yOrigin, width=2, arrow=tk.FIRST)
        #I don't think I need an update here, but I'm not sure.
        

    def setViewAngle(self, vdWindow, thetaViewNew, phiViewNew):
        self.aInCanvas.delete(self.lineA)
        self.thetaView=thetaViewNew
        self.phiView=phiViewNew
        #UNFINISHED
        #More math needed here...
        #reset the axes in this view...
        #reset lineA in this view
        vdWindow.update()

if __name__=="__main__":
    vecWidget=tk.Tk()
    vecWidg=VectorDisplay(vecWidget)
    vecWidg.pack()
