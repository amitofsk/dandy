#This is a child of MCDisplay for drawing an Arduino Nano Every.
#Reference on the pinout:
#https://store-usa.arduino.cc/products/arduino-nano-every
#Dimensions are 45x18mm

import tkinter as tk
import src.widgets.MCDisplay as mcd

class ANanoEveryDisplay(mcd.MCDisplay):
    def __init__(self, windowP):
        super().__init__(windowP)
        self.redraw_body()
        windowP.update


    def redraw_body(self):
        self.mc_canvas.delete(self.rect1)
        self.mc_canvas.delete(self.rect2)
        self.rect1=self.mc_canvas.create_rectangle(246, 165, 354, 435,\
                    fill="green", outline="")
        self.rect2=self.mc_canvas.create_rectangle(280,155,320,185,\
                    fill="gray", outline="")


    


if __name__=="__main__":
    nano_example=tk.Tk()
    nano_widget=ANanoEveryDisplay(nano_example)
    nano_widget.pack()
