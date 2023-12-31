#This example demonstrates GUI widgets that can be used to display
#analog input values. It does not involve any hardware.
#When you run this example, you see a slider widget and four widgets for
#displaying analog values. The slider widget comes from tk while the
#other widgets are part of Dandy.
#The slider widget is


import tkinter as tk
import sys 
sys.path.append('../widgets') 
import DialDisplay as dd 
import SlideDisplay as sd 
import TricolorDisplay as td
import SimplePlotDisplay as spd

 
class SingleAInDemo(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.button_quit=tk.Button(self, text="Quit", \
                            command=self.destroy)
        self.button2=tk.Button(self, text="Get value", \
                            command=self.get_value)
        self.label1=tk.Label(self, text="Hello")
        self.scale1=tk.Scale(self, from_=0, to=10, \
                            orient=tk.HORIZONTAL, length=200, resolution=0.1)   
        self.dial1=dd.DialDisplay(self, \
                            height=100, width=100)
        self.slide1=sd.SlideDisplay(self, width=100, \
                            height=100)
        self.tric1=td.TricolorDisplay(self, width=100, \
                            height=100)
        self.plot1=spd.SimplePlotDisplay(self)
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
