#This is a child of MCDisplay for drawing an Arduino Uno.
#Reference on the pinout https://docs.arduino.cc/hardware/uno-rev3
#Dimensions are 53.4mmx 68.6mm

import tkinter as tk
import sys 
sys.path.append ('../widgets')  
import MCDisplay as mcd  
import LEDDisplay as ld  
import SymbolDisplay as sd  

class AUnoDisplay(mcd.MCDisplay):
    def __init__(self, windowP):
        super().__init__(windowP, leftPins=14, rightPins=18, widgetSize=20)
        self.draw_pwr_gnd()
        #We don't run tkinter in a loop. Instead, we just updat it once.
        windowP.update


    def redraw_body(self):
        self.mc_canvas.create_window(110, 190, window=self.get_left_bar_frame(),\
                            anchor="nw")
        self.mc_canvas.create_window(470, 105, window=self.get_right_bar_frame(),\
                       anchor="nw")
        self.rect1=self.mc_canvas.create_rectangle(141, 94, 459, 506,\
                    fill="teal", outline="")
        self.rect2=self.mc_canvas.create_rectangle(340,70,410,160,\
                    fill="gray", outline="")


    def draw_pwr_gnd(self):
        #The Arduino Uno pins 6, 7, and 29 are ground.
        #Pin 4 is 3.3V power, pin 5 is 5V power, and pin 8 is VIN power.
        counter=1
        for ii in self.get_left_bar():
            ii.pin_number=counter
            if ((counter==6)or(counter==7)):
                ii.draw_ground()
            if(counter==4):
                ii.draw_power(volts=3.3)
            if(counter==5):
                ii.draw_power(volts=5.0)
            if(counter==8):
                ii.draw_power(volts=0)               
            counter=counter+1
            ii.pack()
        counter=32
        for kk in self.get_right_bar():
            kk.pin_number=counter
            if ((counter==29)):
                kk.draw_ground()
            counter=counter-1
            kk.pack()


if __name__=="__main__":
    uno_example=tk.Tk()
    uno_widget=AUnoDisplay(uno_example)
    uno_widget.pack()
