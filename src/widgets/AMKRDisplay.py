#This is a child of MCDisplay for drawing an Arduino MKR1010.
#Reference on the pinout
#https://store-usa.arduino.cc/products/arduino-mkr-wifi-1010
#Dimensions are 61.5x25mm




 
import tkinter as tk
import sys 
sys.path.append ('../widgets')  
import MCDisplay as mcd  
import LEDDisplay as ld  
import SymbolDisplay as sd  

class AMKRDisplay(mcd.MCDisplay):
    def __init__(self, windowP):
        super().__init__(windowP, leftPins=14, rightPins=14, widgetSize=28)
        self.draw_pwr_gnd()
        #We don't run tkinter in a loop. Instead, we just updat it once.
        windowP.update


    def redraw_body(self):
        self.mc_canvas.create_window(165, 150, window=self.get_left_bar_frame(),\
                            anchor="nw")
        self.mc_canvas.create_window(410, 150, window=self.get_right_bar_frame(),\
                       anchor="nw")
        self.rect1=self.mc_canvas.create_rectangle(200, 54, 400, 560,\
                    fill="teal", outline="")
        self.rect2=self.mc_canvas.create_rectangle(265,45,335,90,\
                    fill="gray", outline="")


    def draw_pwr_gnd(self):
        #The Arduino MKR pin 25 is ground.
        #Pin 26 is 3.3V power, pin 28 is 5V power, and pin 27 is VIN power.
        counter=1
        for ii in self.get_left_bar():
            ii.pin_number=counter
            counter=counter+1
            ii.pack()
        counter=28
        for kk in self.get_right_bar():
            kk.pin_number=counter
            if ((counter==25)):
                kk.draw_ground()
            if ((counter==26)):
                kk.draw_power(volts=3.3)
            if ((counter==27)):
                kk.draw_power(volts=0)
            if ((counter==28)):
                kk.draw_power(volts=5.0)
            counter=counter-1
            kk.pack()

    

if __name__=="__main__":
    mc_example=tk.Tk()
    mc_widget=AMKRDisplay(mc_example)
    mc_widget.pack()

