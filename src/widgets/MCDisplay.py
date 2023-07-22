#This class will be used to display multiple inputs along with a picture
#of a microcontroller. Eventually, I want to write some child classes
#that show specific microcontrollers. This class describes a generic
#microcontroller.

#This is eventually going to be an abstract class... Only its children will be
#used?

#Eventually, I'd like this to have the following children:
#RPi, RPiPico, Infineon microcontroller
#Arduinos Uno, MKR1010, and Nano Every?

import tkinter as tk
import sys
sys.path.append ('../widgets') #Veronica
#import src.widgets.LEDDisplay as ld #Veronica
#import src.widgets.SymbolDisplay as sd #Veronica

class MCDisplay:
    def __init__(self, windowMC):
        self.mc_canvas=tk.Canvas(windowMC, height=600, width=600)
        self.rect1=self.mc_canvas.create_rectangle(120,50, 180,250, fill="green",\
                       outline="")
        self.rect2=self.mc_canvas.create_rectangle(140, 40, 170, 70, \
                        fill="gray", outline="")

       
        #self.left_bar_frame=tk.Frame(windowMC)
        #self.left_bar=[ld.LEDDisplay(self.left_bar_frame, height=25,width=25),\
        #            ld.LEDDisplay(self.left_bar_frame, height=25,width=25),\
        #            sd.SymbolDisplay(self.left_bar_frame, height=25, width=25),
        #            ld.LEDDisplay(self.left_bar_frame, height=25,width=25)]
        #for ii in self.left_bar:
        #    ii.pack()
        #    if isinstance(ii, ld.LEDDisplay)==True:
        #        ii.change_LED_color("purple")
        #self.mc_canvas.create_window(50,50, window=self.left_bar_frame, anchor="nw")
        
      
        windowMC.update()

    
      
    def pack(self):
        self.mc_canvas.pack()

    def toggle_one_pin(self, pin):
        print("coming soon")

if __name__=="__main__":
    mc_example=tk.Tk()
    mc_widget=MCDisplay(mc_example)
    mc_widget.pack()
        
        

        
