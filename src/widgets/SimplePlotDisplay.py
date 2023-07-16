#I want to display analog inputs as plots vs. time. I'm not sure
#if I should write this myself or if I should use matplotlib and numpy.
#I'll try both ways. This file is for the version I write myself.
#Maybe I'll eventually want to include both...
#This class is for displaying analog inputs. It is a child of
#AnalogInDisplay. Here I'm writing plotting code myself...


#This is very unfinished ...


import tkinter as tk
import src.widgets.AnalogInDisplay as ain

max_points=25

class SimplePlotDisplay(ain.AnalogInDisplay):
    def __init__(self, windowP, height=100, width=100):
        super().__init__(windowP, a_height=height, a_width=width)
        self.axisX=self.ain_canvas.create_line(0.1*width, 0.9*height, \
                        0.9*width,0.9*height, fill="blue", arrow=tk.LAST)
        self.axisY=self.ain_canvas.create_line(0.1*width, 0.9*height,\
                        0.1*width,0.1*height, fill="blue",arrow=tk.LAST)
        self.labelX=self.ain_canvas.create_text(0.95*width, 0.95*height, \
                        text="t")
        self.curr_point=0
        self.data_values=[3.0]*max_points
        self.data_points=[self.ain_canvas.create_oval(.1*width,\
                        0.1*height,0.1*width,0.1*height)]*max_points
        for jj in range(max_points):
            self.data_points[jj]=self.ain_canvas.create_oval((0.1*width+jj*3),
                    0.9*height-10*self.data_values[jj], \
                    ((0.1*width+jj*3))+2, (0.9*height-\
                    10*self.data_values[jj])+2, fill="green")
        
        windowP.update()





    def add_point(self, valueA):
        self.data_values[self.curr_point]=valueA
        self.ain_canvas.delete(self.data_points[self.curr_point])
        self.data_points[self.curr_point]=self.ain_canvas.create_oval(\
                    (0.1*self.ain_width+self.curr_point*3),
                    0.9*self.ain_height-10*self.data_values[self.curr_point], \
                    ((0.1*self.ain_width+self.curr_point*3))+2, \
                    (0.9*self.ain_height-10*self.data_values[self.curr_point])\
                    +2, fill="green")
        self.curr_point=(self.curr_point+1)%max_points
       


    
        




if __name__=="__main__":
    plot_example=tk.Tk()
    plot_widget=SimplePlotDisplay(plot_example)
    plot_widget.pack()



