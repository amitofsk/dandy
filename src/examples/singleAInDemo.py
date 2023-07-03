#This example just demonstrates GUI widgets that can be used to display
#analog input values. Here I'm not actually integrate with any analog input.
#Instead, I just use a slider. I demonstrate a numerical readout,
#a needle on a dial and a chart plot. All of this uses tkinter

#After I get this working, the next step is to break the widgets into separate files
#and incorporate them into the main example cleanly.

import tkinter as tk
import sys
sys.path.append('../widgets')

import DialDisplay
import SlideDisplay




class SingleAInDemo:
    def __init__(self):
        self.main_window=tk.Tk()
        self.buttonQuit=tk.Button(self.main_window, text="Quit", command=self.main_window.destroy)
        self.button2=tk.Button(self.main_window, text="Get value", command=self.getValue)
        self.label1=tk.Label(self.main_window, text="Hello")
        self.scale1=tk.Scale(self.main_window, from_=0, to=10, orient=tk.HORIZONTAL, \
                             length=200, resolution=0.1)   
        self.dial1=DialDisplay.DialDisplay(self.main_window)
        self.slide1=SlideDisplay.SlideDisplay(self.main_window)

        self.label1.pack()
        self.scale1.pack()
        self.slide1.pack()
        self.dial1.pack()
        self.button2.pack()
        self.buttonQuit.pack()
        

        #Main loop
        tk.mainloop()


    def getValue(self):
        slideValue="Value ="+str(self.scale1.get())
        self.label1.config(text=slideValue)
        self.dial1.setToValue(self.scale1.get())
        self.slide1.setToValue(self.scale1.get())




if __name__=="__main__":
    mygui=SingleAInDemo()
