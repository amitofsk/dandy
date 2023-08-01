#This is a child of MCDisplay specifically for drawing RPi Picos.
#Reference on RPi Pico Pinout:
# https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf
#It is 51x21mm.

import tkinter as tk
import sys  
sys.path.append ('../widgets')  
import MCDisplay as mcd  
import LEDDisplay as ld  
import SymbolDisplay as sd  

class RPiPicoDisplay(mcd.MCDisplay):
    def __init__(self, windowP):
        super().__init__(windowP, leftPins=20, rightPins=20, widgetSize=19)
        self.draw_pwr_gnd()
        #We don't run tkinter in a loop. Instead, we just updat it once.
        windowP.update


    def redraw_body(self):
        self.mc_canvas.create_window(190, 88, window=self.get_left_bar_frame(),\
                            anchor="nw")
        self.mc_canvas.create_window(390, 88, window=self.get_right_bar_frame(),\
                       anchor="nw")
        self.rect1=self.mc_canvas.create_rectangle(216, 96, 384, 504,\
                    fill="green", outline="")
        self.rect2=self.mc_canvas.create_rectangle(270,80,330,120,\
                    fill="gray", outline="")

       
    def draw_pwr_gnd(self):
        #The RPiPico pins 3, 8, 13, 18, 23, 28, 33, and 38 are ground.
        #Pin 36 is 3.3V power, pin 39 is VSYS power, and pin 40 is VBUS power.
        counter=1
        for ii in self.get_left_bar():
            ii.pin_number=counter
            if ((counter==3)or(counter==8)or(counter==13)or(counter==18)):
                ii.draw_ground()
            counter=counter+1
            ii.pack()
        counter=40
        for kk in self.get_right_bar():
            kk.pin_number=counter
            if ((counter==23)or(counter==28)or(counter==33)or(counter==38)):
                kk.draw_ground()
            if(counter==36):
                kk.draw_power(volts=3.3)
            if(counter==39):
                kk.draw_power(volts=0)
            if(counter==40):
                kk.draw_power(volts=5.0)            
            counter=counter-1
            kk.pack()



if __name__=="__main__":
    rp_example=tk.Tk()
    rp_widget=RPiPicoDisplay(rp_example)
    rp_widget.pack()
    rp_widget.set_led(9)
    rp_widget.set_led_color(9)
    rp_widget.set_led(26)
    rp_widget.set_led_color(26, "purple")
    rp_widget.set_button(10)
     
    
        

