#I want to display analog inputs as plots vs. time. I'm not sure
#if I should write this myself or if I should use matplotlib and numpy.
#I'll try both ways. This file is for the version I write myself.
#Maybe I'll eventually want to include both...
#This class is for displaying analog inputs. It is a child of
#AnalogInDisplay. Here I'm writing plotting code myself...


#This is very unfinished ...

import tkinter as tk
import AnalogInDisplay as ain

class SimplePlotDisplay(ain.AnalogInDisplay):
    def __init__(self, windowP, height=100, width=100):
        super().__init__(windowP, a_height=height, a_width=width)
        self.axisX=self.ain_canvas.create_line(0.1*width, 0.9*height, \
                        0.9*width,0.9*height, fill="blue", arrow=tk.LAST)
        self.axisY=self.ain_canvas.create_line(0.1*width, 0.9*height,\
                        0.1*width,0.1*height, fill="blue",arrow=tk.LAST)

        windowP.update()




if __name__=="__main__":
    plot_example=tk.Tk()
    plot_widget=SimplePlotDisplay(plot_example)
    plot_widget.pack()



