#THIS FILE WILL BE CUT SOON

#This is a child of MCDisplay for drawing a RPi.
#Reference on the pinout
# https://randomnerdtutorials.com/raspberry-pi-pinout-gpios/
#Dimensions are 56x85mm

import tkinter as tk
import sys # Veronica 
sys.path.append ('../widgets') #Veronica
import MCDisplay as mcd #Veronica

class RPiDisplay(mcd.MCDisplay):
    def __init__(self, windowP):
        super().__init__(windowP)
        self.redraw_body()
        windowP.update


    def redraw_body(self):
        self.mc_canvas.delete(self.rect1)
        self.mc_canvas.delete(self.rect2)
        self.rect1=self.mc_canvas.create_rectangle(188, 130, 412, 470,\
                    fill="green", outline="")
        self.rect2=self.mc_canvas.create_rectangle(280,120,340,170,\
                    fill="gray", outline="")


    


if __name__=="__main__":
    rp_example=tk.Tk()
    rp_widget=RPiDisplay(rp_example)
    rp_widget.pack()
