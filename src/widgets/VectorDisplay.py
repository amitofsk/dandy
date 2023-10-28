#This class displays three numeric values, such as from analog inputs (x,y,z)
#components of analog sensors, as an vector.
#It is a child of AnalogInDisplay.

#Reference on Isometric Projection: https://en.wikipedia.org/wiki/Isometric_projection
#Let's start by assuming a viewing angle of theta=45 and phi=45. Later I can
#generalize this...

#Watch the minus signs carefully here, positive x is to the LEFT, (origin - newXValue).
#However, positive y is DOWN, so (origin-newYValue).
#I think I finally got the minus signs working here...


import tkinter as tk
import math  
import AnalogInDisplay as ain


class VectorDisplay(ain.AnalogInDisplay):
    def __init__(self, windowV, height=100, width=100):
        super().__init__(windowV, a_height=height, a_width=width)
        self.__xOrigin=0.5*self.get_ain_width()
        self.__yOrigin=0.5*self.get_ain_height()
        #radius_scale_factor sets the fraction of the window used by the widget.
        self.__radius_scale_factor=0.75 
        if height<width:
            self.__radius=0.5*self.__radius_scale_factor*self.get_ain_height()
        else:
            self.__radius=0.5*self.__radius_scale_factor*self.get_ain_width()
      
        self.__theta_view=math.radians(45) 
        self.__phi_view=math.radians(225)
        self.__axisX=self.ain_canvas.create_line(self.__xOrigin, self.__yOrigin, \
                    (self.__xOrigin-(math.cos(self.__theta_view)*self.__radius)), \
                    (self.__yOrigin-(math.sin(self.__theta_view) \
                    *math.sin(self.__phi_view)*self.__radius)), \
                    arrow=tk.LAST)
        self.__axisY=self.ain_canvas.create_line(self.__xOrigin, self.__yOrigin, \
                    self.__xOrigin, (self.__yOrigin-self.__radius\
                    *math.cos(self.__phi_view)), arrow=tk.LAST)
        self.__axisZ=self.ain_canvas.create_line(self.__xOrigin,self.__yOrigin , \
                    (self.__xOrigin-(-math.sin(self.__theta_view)*self.__radius)), \
                    (self.__yOrigin-(math.sin(self.__phi_view) \
                    *math.cos(self.__theta_view)*self.__radius)), \
                    arrow=tk.LAST)
        self.__lineA=self.ain_canvas.create_line(self.__xOrigin+self.__radius, \
                    self.__yOrigin+self.__radius, self.__xOrigin, self.__yOrigin, \
                    width=2, arrow=tk.FIRST, fill=self.get_color1())
        self.__labelX=self.ain_canvas.create_text(0.3*width, 0.75*height, \
                    text="X", fill=self.get_color1())
        self.__labelY=self.ain_canvas.create_text(0.5*width, 0.9*height, \
                    text="Y", fill=self.get_color1())
        self.__labelZ=self.ain_canvas.create_text(0.7*width, 0.75*height, \
                    text="Z", fill=self.get_color1())

        windowV.update()

 


    def set_to_value(self, xValue, yValue, zValue):
        positionX=0.0
        positionY=0.0
        self.ain_canvas.delete(self.__lineA)
        projectedX=(xValue*math.cos(self.__theta_view))- \
                    (zValue*math.sin(self.__theta_view))
        projectedY=(xValue*math.sin(self.__phi_view)*math.sin(self.__theta_view)) \
                    +(yValue*math.cos(self.__phi_view)) \
                    +(zValue*math.sin(self.__phi_view)\
                    *math.cos(self.__theta_view))
        positionX=self.__xOrigin-projectedX
        positionY=self.__yOrigin-projectedY 
        self.__lineA=self.ain_canvas.create_line(positionX, positionY, \
                    self.__xOrigin, self.__yOrigin, width=2, arrow=tk.FIRST, \
                    fill=self.get_color1())
       
        

    def setViewAngle(self, windowV, theta_new, phi_new):
        self.ain_canvas.delete(self.lineA)
        self.__theta_view=theta_new
        self.__phi_view=phi_new
        #UNFINISHED
        #More math needed here...
        #reset the axes in this view...
        #reset lineA in this view
        windowV.update()


if __name__=="__main__":
    vec_example=tk.Tk()
    vec_widget=VectorDisplay(vec_example)
    vec_widget.pack()
