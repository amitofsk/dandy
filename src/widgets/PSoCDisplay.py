#This is a child of MCDisplay for drawing the CY8cProto
#Reference on the pinout
# https://www.infineon.com/dgdl/Infineon-CY8CPROTO-062-4343W_PSoC_6_Wi-Fi_BT_Prototyping_Kit_Guide-UserManual-v01_00-EN.pdf?fileId=8ac78c8c7d0d8da4017d0f0118571844

import tkinter as tk
import sys 
sys.path.append ('../widgets')  
import MCDisplay as mcd  
import LEDDisplay as ld  
import SymbolDisplay as sd  

class PSoCDisplay(mcd.MCDisplay):
    def __init__(self, windowP):
        super().__init__(windowP, leftPins=43, rightPins=40, widgetSize=10)
        self.draw_pwr_gnd()
        #We don't run tkinter in a loop. Instead, we just updat it once.
        windowP.update


    def redraw_body(self):
        self.mc_canvas.create_window(220, 30, window=self.get_left_bar_frame(),\
                            anchor="nw")
        self.mc_canvas.create_window(370, 70, window=self.get_right_bar_frame(),\
                       anchor="nw")
        self.rect1=self.mc_canvas.create_rectangle(240, 30, 360, 550,\
                    fill="teal", outline="")
        self.rect2=self.mc_canvas.create_rectangle(280,25,320,55,\
                    fill="gray", outline="")

     
    def draw_pwr_gnd(self):
        #The PSoC pins 2, 4, 31, 36, 53, 61, 74, and 82 are ground.
        #Pins 1, 3, 5, 24, 35, 52, 54, 60, 81, and 83 are power.
        counter=1
        for ii in self.get_left_bar():
            ii.pin_number=counter
            if ((counter==2)or(counter==4)or(counter==31)or(counter==36)):
                ii.draw_ground()
            if((counter==1)or(counter==3)or(counter==24)or(counter==35)):
                ii.draw_power(volts=0)               
            counter=counter+1
            ii.pack()
        counter=83
        for kk in self.get_right_bar():
            kk.pin_number=counter
            if ((counter==53)or(counter==61)or(counter==74)or(counter==82)):
                kk.draw_ground()
            if ((counter==52)or(counter==54)or(counter==60)or \
                (counter==81)or(counter==83)):
                kk.draw_power(volts=0)
            counter=counter-1
            kk.pack()


if __name__=="__main__":
    mc_example=tk.Tk()
    mc_widget=PSoCDisplay(mc_example)
    mc_widget.pack()
