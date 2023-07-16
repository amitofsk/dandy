#This file just demonstrates GUI widgets that can be used to display
#Digital input values. Here I'm not actually integrating with hardware.
#Instead, I just stub the input with a button.


import tkinter as tk
#import sys
#sys.path.append('../widgets')
import src.widgets.LEDDisplay as ld
import src.widgets.LEDBarDisplay as ld_bar


class DInDemo:
    def __init__(self):
        self.main_window=tk.Tk()
        self.button_quit=tk.Button(self.main_window, text="Quit", \
                            command=self.main_window.destroy)
        self.button2=tk.Button(self.main_window, text="Toggle", \
                            command=self.getValue)
        #self.led1=LEDDisplay.LEDDisplay(self.main_window)
        self.bar1=ld_bar.LEDBarDisplay(self.main_window, led_count=3)

        self.button2.pack()
        #self.led1.pack()
        self.bar1.pack()
        self.button_quit.pack()

        tk.mainloop()

    def getValue(self):
        #if(self.led1.LED_color=="yellow"):
        #    self.led1.change_LED_color("blue")
        #elif (self.led1.LED_color=="blue"):
        #    self.led1.change_LED_color("yellow")
       # self.led1.change_BG_color("orange")
        self.bar1.set_color_one(0)

if __name__=="__main__":
    mygui=DInDemo()
        
