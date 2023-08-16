#This example demonstrates the KnobDisplay and SlideDisplay widgets.
#Put your cursor over the KnobDisplay widget and scroll the middle mouse button.

##TODO: When you press quit, you get an error from slideDisplay.
#Can I clean this up?

import tkinter as tk
import sys
sys.path.append('../widgets') 
import KnobDisplay as kd 
import SlideDisplay as sd

class KnobDemo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.canvasK=tk.Canvas(self, height=300, width=300)
        self.button_quit=tk.Button(self, text="Quit", \
                            command=self.destroy)
        self.slide1=sd.SlideDisplay(self, width=100, \
                            height=100)
        self.knob1=kd.KnobDisplay(self.canvasK, width=100, height=100)

        self.offset=5
        self.value=0
        self.canvasK.pack()
        self.knob1.pack()
        self.slide1.pack()
        self.button_quit.pack()

        #We don't run Tkinter's main loop. Instead, we run the function
        #updater, which we define below. That function manually updates
        #the Tkinter loop.
        self.updater()


    def updater(self):
        while True:
            print(self.value)
            self.value=self.offset+self.knob1.get_angle()
            self.slide1.set_to_value(self.value)    
            self.update()
            

if __name__=="__main__":
    mygui=KnobDemo()
