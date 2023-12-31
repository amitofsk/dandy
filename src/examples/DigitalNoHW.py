#This example demonstrates how to use widgets in the DANDY library.
#When you run it, you will see a window with two buttons and a LEDDisplay object.
#When you press the button, you toggle the LED color.

import tkinter as tk
import sys
#We need to import the file for the LEDDisplay widget
#You may need to change the next line so it points to the correct directory.
sys.path.append('../widgets')
import LEDDisplay as ld

class DigitalNoHW(tk.Tk):
    def __init__(self):
        super().__init__()
        #The class LEDDisplay is defined in the file ../widgets/LEDDisplay.py
        self.led1=ld.LEDDisplay(self)
        self.button1=tk.Button(self, text="Press Me", \
                               command=self.toggle_me)
        self.button_quit=tk.Button(self, text="Quit", \
                                   command=self.destroy)

        self.led1.pack()
        self.button1.pack()
        self.button_quit.pack()

        tk.mainloop()

        
    #Here we define the toggle_me function
    def toggle_me(self):
        if(self.led1.get_color()=="yellow"):
            self.led1.change_LED_color("blue")
        else:  
            self.led1.change_LED_color("yellow")


if __name__=="__main__":
    mygui=DigitalNoHW()

