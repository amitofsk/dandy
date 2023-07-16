#This is a child of MCDisplay for drawing an Arduino MKR1010.
#Reference on the pinout
#https://store-usa.arduino.cc/products/arduino-mkr-wifi-1010
#Dimensions are 61.5x25mm

import tkinter as tk
import src.widgets.MCDisplay as mcd

class AMKRDisplay(mcd.MCDisplay):
    def __init__(self, windowP):
        super().__init__(windowP)
        self.redraw_body()
        windowP.update


    def redraw_body(self):
        self.mc_canvas.delete(self.rect1)
        self.mc_canvas.delete(self.rect2)
        self.rect1=self.mc_canvas.create_rectangle(225, 116, 375, 484,\
                    fill="green", outline="")
        self.rect2=self.mc_canvas.create_rectangle(280,110,320,140,\
                    fill="gray", outline="")


    


if __name__=="__main__":
    mkr_example=tk.Tk()
    mkr_widget=AMKRDisplay(mkr_example)
    mkr_widget.pack()
