#This example is used to test the RPiPicoDisplay class. 
#When you run this example, you will see a RPiPicoDisplay widget.
#Pin 6 is set to an LED and pin 26 is set to a button.
#If you press either the button at pin 26 or the toggle button at
#the bottom, the color of the LED at pin 6 changes.


import tkinter as tk
import sys  
sys.path.append('../widgets') 
import MCDisplay as mcd  
import RPiPicoDisplay as rpp
import SymbolDisplay as sd

class MCDemo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.button_quit=tk.Button(self, text="Quit", \
                                   command=self.destroy) 
        self.button2=tk.Button(self, text="Toggle",\
                               command=self.go_button)
        self.pico1=rpp.RPiPicoDisplay(self)
        self.pico1.pack()
        self.button2.pack()
        self.button_quit.pack()

        #Let's add an LED at pin 6
        self.pico1.set_led(6)

        #Let's add a button at pin 26
        self.button3=self.pico1.set_button(26)
        self.button3.bind('<ButtonPress>',self.go_button2)
        
        #Run tkinter's main loop
        tk.mainloop()

    #When the toggle button is pressed, we follow the instructions in go_button.
    def go_button(self):
        if(self.pico1.get_led_color(6)=="yellow"):
            self.pico1.set_led_color(6, "blue")
        else:
            self.pico1.set_led_color(6, "yellow")

    #When the button at pin 26 is pressed, we follow instructions in go_button2.
    #I need an extra input here for some reason.
    def go_button2(self, x):
        if(self.pico1.get_led_color(6)=="yellow"):
            self.pico1.set_led_color(6, "blue")
        else:
            self.pico1.set_led_color(6, "yellow")
        
        
if __name__=="__main__":
    mygui=MCDemo()
