#This class draws static symbols like ground and 5V.
#It is used by the MCDisplay class.

import tkinter as tk


class SymbolDisplay:
    def __init__(self, windowS, height=75, width=75):
        self.height=height
        self.width=width
        self.canvasS=tk.Canvas(windowS, height=self.height, width=self.width)
        self.draw_power(volts=3.3)
        self.pin_number=0
        self.draw_box()

    def pack(self):
        self.canvasS.pack()

    def destroy(self):
        self.canvasS.destroy()

    def pack_forget(self):
        self.canvasS.pack_forget()


    def draw_power(self, volts=5.0):
        self.canvasS.delete('all')
        self.canvasS.create_oval(0.1*self.width, 0.1*self.height,\
                        0.9*self.width, 0.9*self.height, fill="red", outline="")
        self.canvasS.create_text(0.5*self.width, 0.5*self.height,\
                        fill="white", text=volts)
       

    def draw_ground(self):
        self.canvasS.delete('all')
        self.canvasS.create_line(0.5*self.width,0.1*self.height,\
                        0.5*self.width,0.5*self.height, fill="black", width=3)
        self.canvasS.create_line(0.1*self.width, 0.5*self.height,\
                        0.9*self.width, 0.5*self.height, fill="black", width=3)
        self.canvasS.create_line(0.3*self.width, 0.7*self.height,\
                        0.7*self.width, 0.7*self.height, fill="black", width=3)
        self.canvasS.create_line(0.4*self.width, 0.9*self.height,\
                        0.6*self.width, 0.9*self.height, fill="black", width=3)
        
        
    def draw_box(self):
        self.canvasS.delete('all')
        self.canvasS.create_rectangle(0.2*self.width, 0.2*self.height,\
                        0.8*self.width, 0.8*self.height, fill="gray")

if __name__=="__main__":
    s_example=tk.Tk()
    s_widget=SymbolDisplay(s_example, height=25, width=25)
    s_widget.pack()
