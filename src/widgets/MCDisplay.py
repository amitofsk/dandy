#This class will be used to display multiple inputs along with a picture
#of a microcontroller. Eventually, I want to write some child classes
#that show specific microcontrollers. This class describes a generic
#microcontroller.

import tkinter as tk
import LEDDisplay

class MCDisplay:
    def __init__(self, windowMC):
        self.mc_canvas=tk.Canvas(windowMC, height=300, width=300)
        self.rect1=self.mc_canvas.create_rectangle(120,50, 180,250, fill="green",\
                                                outline="")
      
        windowMC.update()

    def pack(self):
        self.mc_canvas.pack()

if __name__=="__main__":
    mc_example=tk.Tk()
    mc_widget=MCDisplay(mc_example)
    mc_widget.pack()
        
        

        
