#This is a child of MCDisplay for drawing an Arduino Nano Every.
#Reference on the pinout:
#https://store-usa.arduino.cc/products/arduino-nano-every
#Dimensions are 45x18mm

import tkinter as tk
import sys 
sys.path.append ('../widgets')  
import MCDisplay as mcd  
import LEDDisplay as ld  
import SymbolDisplay as sd  

class ANanoEveryDisplay(mcd.MCDisplay):
    def __init__(self, windowP):
        super().__init__(windowP, leftPins=15, rightPins=15, widgetSize=30)
        self.draw_pwr_gnd()
        #We don't run tkinter in a loop. Instead, we just updat it once.
        windowP.update


    def redraw_body(self):
        self.mc_canvas.create_window(190, 60, window=self.get_left_bar_frame(),\
                            anchor="nw")
        self.mc_canvas.create_window(380, 60, window=self.get_right_bar_frame(),\
                       anchor="nw")
        self.rect1=self.mc_canvas.create_rectangle(228, 40, 372, 560,\
                     fill="teal", outline="")
        self.rect2=self.mc_canvas.create_rectangle(260,30,340,60,\
                    fill="gray", outline="")


    def draw_pwr_gnd(self):
        #The Arduino Nano Every pins 14 and 19 are ground.
        #Pin 2 is 3.3V power, pin 12 is 5V power, and pin 15 is VIN power.
        counter=1
        for ii in self.get_left_bar():
            ii.pin_number=counter
            if ((counter==14)):
                ii.draw_ground()
            if(counter==2):
                ii.draw_power(volts=3.3)
            if(counter==12):
                ii.draw_power(volts=5.0)
            if(counter==15):
                ii.draw_power(volts=0)               
            counter=counter+1
            ii.pack()
        counter=30
        for kk in self.get_right_bar():
            kk.pin_number=counter
            if ((counter==199)):
                kk.draw_ground()
            counter=counter-1
            kk.pack()

    
if __name__=="__main__":
    mc_example=tk.Tk()
    mc_widget=ANanoEveryDisplay(mc_example)
    mc_widget.pack()

