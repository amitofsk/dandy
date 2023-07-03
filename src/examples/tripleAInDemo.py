#This example demonstrates GUI widgets used to display three naalog inputs.


import tkinter as tk
import sys
sys.path.append('../widgets')
import VectorDisplay
import DialDisplay

class TripleAInDemo:
    def __init__(self):
        self.main_window=tk.Tk()
        self.buttonQuit=tk.Button(self.main_window, text="Quit", command=self.main_window.destroy)
        self.button2=tk.Button(self.main_window, text="Get Value", command=self.getValue)
        self.label1=tk.Label(self.main_window, text="Hi")
        self. scaleX=tk.Scale(self.main_window, from_=0, to=50, orient=tk.HORIZONTAL, \
                              length=200, resolution=0.1)
        self.scaleY=tk.Scale(self.main_window, from_=0, to=50, orient=tk.HORIZONTAL, \
                             length=200, resolution=0.1)
        self.scaleZ=tk.Scale(self.main_window, from_=0, to=50, orient=tk.HORIZONTAL, \
                             length=200, resolution=0.1)
        self.vectorD=VectorDisplay.VectorDisplay(self.main_window)

        self.label1.pack()
        self.scaleX.pack()
        self.scaleY.pack()
        self.scaleZ.pack()
        self.vectorD.pack()
        self.button2.pack()
        self.buttonQuit.pack()

        #Main loop
        tk.mainloop()

    def getValue(self):
        xValueStr="X Value="+str(self.scaleX.get())
        self.label1.config(text=xValueStr)
        self.vectorD.setToValue(self.scaleX.get(), self.scaleY.get(), self.scaleZ.get())

if __name__=="__main__":
    mygui=TripleAInDemo()
        
