#This widget displays analog input variables as a plot.
#This plot is limited and not very fancy. If you want fancy version,
#write your own widget which is a child of this or something.
#This class is a child of AnalogInDisplay.py.


import tkinter as tk
import sys  
sys.path.append ('../widgets') 
import AnalogInDisplay as ain 

#This sets the points shown horizontally.
max_points=25

class SimplePlotDisplay(ain.AnalogInDisplay):
    def __init__(self, windowP, height=100, width=100):
        super().__init__(windowP, a_height=height, a_width=width)
        self.__axisX=self.ain_canvas.create_line(0.1*width, 0.9*height, \
                        0.9*width,0.9*height, fill="blue", arrow=tk.LAST)
        self.__axisY=self.ain_canvas.create_line(0.1*width, 0.9*height,\
                        0.1*width,0.1*height, fill="blue",arrow=tk.LAST)
        self.__labelX=self.ain_canvas.create_text(0.95*width, 0.95*height, \
                        text="t")
        self.__curr_point=0
        self.__data_values=[3.0]*max_points
        self.__data_points=[self.ain_canvas.create_oval(.1*width,\
                        0.1*height,0.1*width,0.1*height)]*max_points
        for jj in range(max_points):
            self.__data_points[jj]=self.ain_canvas.create_oval((0.1*width+jj*3),
                    0.9*height-10*self.__data_values[jj], \
                    ((0.1*width+jj*3))+2, (0.9*height-\
                    10*self.__data_values[jj])+2, fill="green")
        
        windowP.update()





    def add_point(self, valueA):
        self.__data_values[self.__curr_point]=valueA
        self.ain_canvas.delete(self.__data_points[self.__curr_point])
        self.__data_points[self.__curr_point]=self.ain_canvas.create_oval(\
                    (0.1*self.get_ain_width()+self.__curr_point*3),
                    0.9*self.get_ain_height()-10*self.__data_values[self.__curr_point], \
                    ((0.1*self.get_ain_width()+self.__curr_point*3))+2, \
                    (0.9*self.get_ain_height()-10*self.__data_values[self.__curr_point])\
                    +2, fill="green")
        self.__curr_point=(self.__curr_point+1)%max_points
       


    
        




if __name__=="__main__":
    plot_example=tk.Tk()
    plot_widget=SimplePlotDisplay(plot_example)
    plot_widget.pack()



