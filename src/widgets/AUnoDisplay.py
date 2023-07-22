#This is a child of MCDisplay for drawing an Arduino Uno.
#Reference on the pinout https://docs.arduino.cc/hardware/uno-rev3
#Dimensions are 53.4mmx 68.6mm



import tkinter as tk
import sys # Veronica 
sys.path.append ('../widgets') #Veronica
import MCDisplay as mcd #Veronica
import LEDDisplay as ld #Veronica
import SymbolDisplay as sd #Veronica

class AUnoDisplay(mcd.MCDisplay):
    def __init__(self, windowP):
        super().__init__(windowP)
        self.redraw_body()
        windowP.update
        self.right_frame=tk.Frame(windowP)
        self.bar=[]
        count=1
        for jj in range (18):
            self.bar=self.bar+[ld.LEDDisplay(self.right_frame, \
                        height=15, width=15)]
        for ii in self.bar:
            ii.pin_number=count
            count=count+1
            ii.pack(bar_orientation="vertical")
        self.mc_canvas.create_window(470,180, window=self.right_frame, anchor="nw")
            


    def redraw_body(self):
        self.mc_canvas.delete(self.rect1)
        self.mc_canvas.delete(self.rect2)
        self.rect1=self.mc_canvas.create_rectangle(141, 94, 459, 506,\
                    fill="teal", outline="")
        self.rect2=self.mc_canvas.create_rectangle(340,70,410,160,\
                    fill="gray", outline="")


    


if __name__=="__main__":
    uno_example=tk.Tk()
    uno_widget=AUnoDisplay(uno_example)
    uno_widget.pack()
