#This example demonstrates GUI widgets used to display three analog inputs.


import tkinter as tk
import sys
sys.path.append('../widgets')
import VectorDisplay as vd 

class TripleAInDemo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.button_quit=tk.Button(self, text="Quit", \
                            command=self.destroy)
        self.button2=tk.Button(self, text="Get Value", \
                            command=self.getValue)
        self.label1=tk.Label(self, text="Hi")
        self. scaleX=tk.Scale(self, from_=0, to=50, orient=tk.HORIZONTAL, \
                             length=200, resolution=0.1)
        self.scaleY=tk.Scale(self, from_=0, to=50, orient=tk.HORIZONTAL, \
                             length=200, resolution=0.1)
        self.scaleZ=tk.Scale(self, from_=0, to=50, orient=tk.HORIZONTAL, \
                             length=200, resolution=0.1)
        self.vector1=vd.VectorDisplay(self, height=100, width=200)

        self.label1.pack()
        self.scaleX.pack()
        self.scaleY.pack()
        self.scaleZ.pack()
        self.vector1.pack()
        self.button2.pack()
        self.button_quit.pack()

        #Main loop
        tk.mainloop()


    def getValue(self):
        value_message="X Value="+str(self.scaleX.get())
        self.label1.config(text=value_message)
        self.vector1.set_to_value(self.scaleX.get(), self.scaleY.get(), \
                            self.scaleZ.get())

if __name__=="__main__":
    triple_demo=TripleAInDemo()
        
