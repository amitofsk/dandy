#THIS CLASS WILL BE DELETED SOON

#This class will be used to display multiple inputs along with a picture
#of a microcontroller. Eventually, I want to write some child classes
#that show specific microcontrollers. This class describes a generic
#microcontroller.

#This is eventually going to be an abstract class... Only its children will be
#used?

#Eventually, I'd like this to have the following children:
#RPi, RPiPico, Infineon microcontroller
#Arduinos Uno, MKR1010, and Nano Every?

import tkinter as tk
import sys
sys.path.append ('../widgets')
import LEDDisplay as ld  
import SymbolDisplay as sd  


class MCDisplay:
    def __init__(self, windowMC, left_pins=20, right_pins=20):
        self.mc_canvas=tk.Canvas(windowMC, height=600, width=600)
 #       self.__left_pins=left_pins
 #       self.left_bar_frame=tk.Frame(windowMC)
 #       self.__left_bar=[]
 #       self.__right_pins=right_pins
 #       self.right_bar_frame=tk.Frame(windowMC)
 #       self.__right_bar=[]
 #       for jj in range(self.__left_pins):
 ##           self.__left_bar=self.__left_bar+[sd.SymbolDisplay(\
   #             self.left_bar_frame, height=19, width=19)]
   #     for jj in range(self.__right_pins):
   #         self.__right_bar=self.__right_bar+[sd.SymbolDisplay(\
   #             self.right_bar_frame, height=19, width=19)]
    #    self.mc_canvas.create_window(190, 88, window=self.left_bar_frame,\
    #                        anchor="nw")
    #    self.mc_canvas.create_window(390, 88, window=self.right_bar_frame,\
    #                        anchor="nw")  

        self.redraw_body()
        #self.draw_pwr_gnd()
      
        windowMC.update()

    def redraw_body(self):
        self.rect1=self.mc_canvas.create_rectangle(120,50, 180,250, fill="green",\
                       outline="")
        self.rect2=self.mc_canvas.create_rectangle(140, 40, 170, 70, \
                        fill="gray", outline="")

        
    def draw_pwr_gnd(self):
        print('run child version instead')

    
      
    def pack(self):
        self.mc_canvas.pack()



if __name__=="__main__":
    mc_example=tk.Tk()
    mc_widget=MCDisplay(mc_example)
    mc_widget.pack()
        
        

        
