#This class displays three analog inputs (x,y,z) as an vector.
#It is a child of AnalogInDisplay.

#Reference on Isometric Projection: https://en.wikipedia.org/wiki/Isometric_projection
#Let's start by assuming a viewing angle of theta=45 and phi=45. Later I can generalize this...

#Watch the minus signs carefully here, positive x is to the LEFT, (origin - newXValue).
#However, positive y is DOWN, so (origin-newYValue).
#I think I finally got the minus signs working here...


import tkinter as tk
import math  
import AnalogInDisplay as ain

radiusScaleFactor=0.75

class VectorDisplay(ain.AnalogInDisplay):
    def __init__(self, windowV, height=100, width=100):
        super().__init__(windowV, a_height=height, a_width=width)
        #xOrigin and yOrigin are used in Dial too.
        #Maybe I should move them to AnalogInDisplay?
        self.xOrigin=0.5*self.ain_width
        self.yOrigin=0.5*self.ain_height
        self.radius=radiusScaleFactor*self.xOrigin
        self.theta_view=math.radians(45) 
        self.phi_view=math.radians(225)
        self.axisX=self.ain_canvas.create_line(self.xOrigin, self.yOrigin, \
                    (self.xOrigin-(math.cos(self.theta_view)*self.radius)), \
                    (self.yOrigin-(math.sin(self.theta_view) \
                    *math.sin(self.phi_view)*self.radius)), \
                    fill="blue", arrow=tk.LAST)
        self.axisY=self.ain_canvas.create_line(self.xOrigin, self.yOrigin, \
                    self.xOrigin, (self.yOrigin-self.radius\
                    *math.cos(self.phi_view)), fill="blue", arrow=tk.LAST)
        self.axisZ=self.ain_canvas.create_line(self.xOrigin,self.yOrigin , \
                    (self.xOrigin-(-math.sin(self.theta_view)*self.radius)), \
                    (self.yOrigin-(math.sin(self.phi_view) \
                    *math.cos(self.theta_view)*self.radius)), \
                    fill="blue", arrow=tk.LAST)
        self.lineA=self.ain_canvas.create_line(self.xOrigin+self.radius, \
                    self.yOrigin+self.radius, self.xOrigin, self.yOrigin, \
                    width=2, arrow=tk.FIRST)
        windowV.update()

    #FIXME this has problems if height<width


    def set_to_value(self, xValue, yValue, zValue):
        positionX=0.0
        positionY=0.0
        self.ain_canvas.delete(self.lineA)
        projectedX=(xValue*math.cos(self.theta_view))- \
                    (zValue*math.sin(self.theta_view))
        projectedY=(xValue*math.sin(self.phi_view)*math.sin(self.theta_view)) \
                    +(yValue*math.cos(self.phi_view)) \
                    +(zValue*math.sin(self.phi_view)*math.cos(self.theta_view))
        positionX=self.xOrigin-projectedX
        positionY=self.yOrigin-projectedY 
        self.lineA=self.ain_canvas.create_line(positionX, positionY, self.xOrigin, \
                    self.yOrigin, width=2, arrow=tk.FIRST)
        #I don't think I need an update here, but I'm not sure.
        

    def setViewAngle(self, windowV, theta_new, phi_new):
        self.ain_canvas.delete(self.lineA)
        self.theta_view=theta_new
        self.phi_view=phi_new
        #UNFINISHED
        #More math needed here...
        #reset the axes in this view...
        #reset lineA in this view
        windowV.update()


if __name__=="__main__":
    vec_example=tk.Tk()
    vec_widget=VectorDisplay(vec_example)
    vec_widget.pack()
