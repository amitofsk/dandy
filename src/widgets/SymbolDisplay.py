#This class draws static symbols like ground and 5V.
#It is used by the MCDisplay class.
#To do: Ground north, south, east, and west versions.


import tkinter as tk


class SymbolDisplay():
    def __init__(self, windowS, height=75, width=75):
         
        self.__height=height
        self.__width=width
        self.__canvasS=tk.Canvas(windowS, height=self.__height, width=self.__width)
        self.draw_power(volts=3.3)
        self.__pin_number=0
        self.draw_box()

    def pack(self):
        self.__canvasS.pack()

    def destroy(self):
        self.__canvasS.destroy()

    def pack_forget(self):
        self.__canvasS.pack_forget()


    def draw_power(self, volts=5.0):
        self.__canvasS.delete('all')
        self.__canvasS.create_oval(0.1*self.__width, 0.1*self.__height,\
                        0.9*self.__width, 0.9*self.__height, fill="red", outline="")
        if(volts>0):
            self.__canvasS.create_text(0.5*self.__width, 0.5*self.__height,\
                        fill="white", text=volts)
       

    def draw_ground(self):
        self.__canvasS.delete('all')
        self.__canvasS.create_line(0.5*self.__width,0.1*self.__height,\
                        0.5*self.__width,0.5*self.__height, fill="black", width=3)
        self.__canvasS.create_line(0.1*self.__width, 0.5*self.__height,\
                        0.9*self.__width, 0.5*self.__height, fill="black", width=3)
        self.__canvasS.create_line(0.3*self.__width, 0.7*self.__height,\
                        0.7*self.__width, 0.7*self.__height, fill="black", width=3)
        self.__canvasS.create_line(0.4*self.__width, 0.9*self.__height,\
                        0.6*self.__width, 0.9*self.__height, fill="black", width=3)
        
        
    def draw_box(self):
        self.__canvasS.delete('all')
        self.__canvasS.create_rectangle(0.2*self.__width, 0.2*self.__height,\
                        0.8*self.__width, 0.8*self.__height, fill="gray")

if __name__=="__main__":
    s_example=tk.Tk()
    s_widget=SymbolDisplay(s_example, height=25, width=25)
    s_widget.pack()
