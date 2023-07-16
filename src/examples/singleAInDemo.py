#This example just demonstrates GUI widgets that can be used to display
#analog input values. Here I'm not actually integrate with any analog input.
#Instead, I just use a slider. I demonstrate a numerical readout,
#a needle on a dial and a chart plot. All of this uses tkinter



import tkinter as tk
#FIXME: I should properly set up a package, not use the next two lines.
#import sys
#sys.path.append('../widgets')
#import DialDisplay
#import src.widgets.AnalogInDisplay
import src.widgets.DialDisplay as dd
import src.widgets.SlideDisplay as sd
import src.widgets.TricolorDisplay as td
import src.widgets.SimplePlotDisplay as spd

 


class SingleAInDemo:
    def __init__(self):
        self.main_window=tk.Tk()
        self.button_quit=tk.Button(self.main_window, text="Quit", \
                            command=self.main_window.destroy)
        self.button2=tk.Button(self.main_window, text="Get value", \
                            command=self.get_value)
        self.label1=tk.Label(self.main_window, text="Hello")
        self.scale1=tk.Scale(self.main_window, from_=0, to=10, \
                            orient=tk.HORIZONTAL, length=200, resolution=0.1)   
        self.dial1=dd.DialDisplay(self.main_window, \
                            height=100, width=100)
        self.slide1=sd.SlideDisplay(self.main_window, width=100, \
                            height=100)
        self.tric1=td.TricolorDisplay(self.main_window, width=100, \
                            height=100)
        self.plot1=spd.SimplePlotDisplay(self.main_window)
        self.label1.pack()
        self.scale1.pack()
        self.slide1.pack()
        self.dial1.pack()
        self.tric1.pack()
        self.plot1.pack()
        self.button2.pack()
        self.button_quit.pack()
        
        #Main loop
        tk.mainloop()


    def get_value(self):
        slide_message="Value ="+str(self.scale1.get())
        self.label1.config(text=slide_message)
        self.dial1.set_to_value(self.scale1.get())
        self.slide1.set_to_value(self.scale1.get())
        self.tric1.set_to_value(self.scale1.get())
        self.plot1.add_point(self.scale1.get())


if __name__=="__main__":
    mygui=SingleAInDemo()
