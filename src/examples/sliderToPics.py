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

class AnalogWidgetDisplay:
    def __init__(self):
        self.main_window=tk.Tk()
        self.buttonQuit=tk.Button(self.main_window, text="Quit", command=self.main_window.destroy)
        self.button2=tk.Button(self.main_window, text="Get value", command=self.getValue)
        self.label1=tk.Label(self.main_window, text="Hello")
        self.scale1=tk.Scale(self.main_window, from_=0, to=10, orient=tk.HORIZONTAL, \
                             length=200, resolution=0.1)


        #OK, eventually this will be broken out into a separate file... for now it is here...
        #I'm putting a canvas in a frame. Then, I'm putting a needle on the canvas, static for now.
        self.frame1=tk.Frame(self.main_window)
        #self.canvas1=tk.Canvas(self.dial1, width=100, height=100)
        #self.canvas1.create_line(20,20, 50,80)
        #self.canvas1.pack()
        self.dial1=DialDisplay.DialDisplay(self.frame1)
        self.slide1=SlideDisplay.SlideDisplay(self.frame1)
        
        self.label1.pack()
        self.scale1.pack()
        self.button2.pack()
        self.frame1.pack()
        self.buttonQuit.pack()

        #Main loop
        tk.mainloop()


    def getValue(self):
        slideValue="Value ="+str(self.scale1.get())
        self.label1.config(text=slideValue)
        self.dial1.setToValue(self.frame1, self.scale1.get())
        self.slide1.setToValue(self.frame1, self.scale1.get())




if __name__=="__main__":
    mygui=AnalogWidgetDisplay()
