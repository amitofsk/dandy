#This example draws multiple LEDDisplay or SymbolDisplay widgets
#in a bar. 
#When creating an object of this class, the optional parameter
# orientation can be "vertical" or "horizontal".
#LED_orientation can be "north", "south", "east", or "west".
#The first LED is number 0, not 1.

#TODO: Add functions to change LED orientation, north, south, east, west

import tkinter as tk
import sys 
sys.path.append ('../widgets') 
import LEDDisplay as ld
import SymbolDisplay as sd

class LEDBarDisplay():
    def __init__(self, bar_window, led_count=5, orientation="vertical",\
                 LED_height=50, LED_width=50, LED_orientation="north"):
        self.__d_frame=tk.Frame(bar_window)
        self.__bar=[]
        self.__LED_height=LED_height
        self.__LED_width=LED_width
        self.__orientation=orientation
        count=1
        for jj in range (led_count):
            self.__bar=self.__bar+[ld.LEDDisplay(self.__d_frame, \
                        height=LED_height, width=LED_width,\
                        LED_orientation=LED_orientation)]
        for ii in self.__bar:
            ii.pin_number=count
            count=count+1
            ii.pack(bar_orientation=orientation)
            ii.change_LED_color("blue")


    def pack(self):
        self.__d_frame.pack()


    def pack_forget(self):
        self.__d_frame.pack_forget()


    def set_all_color(self, color="yellow"):
        for ii in self.__bar:
            ii.change_LED_color(color)


    def set_one_color(self, led_number, color="yellow"):
        current_led=self.__bar[led_number]
        current_led.change_LED_color(color)


    def set_gnd(self, pin_no):
        counter=0
        for jj in self.__bar:
            self.__bar[counter].pack_forget()
            if counter==pin_no:
                self.__bar[counter]=sd.SymbolDisplay(self.__d_frame, \
                            height=self.__LED_height, width=self.__LED_width)
                self.__bar[counter].draw_ground()
            self.__bar[counter].pack(bar_orientation=self.__orientation)
            counter=counter+1


    def set_power(self, pin_no, volts=0):
        counter=0
        for jj in self.__bar:
            self.__bar[counter].pack_forget()
            if counter==pin_no:
                self.__bar[counter]=sd.SymbolDisplay(self.__d_frame, \
                            height=self.__LED_height, width=self.__LED_width)
                self.__bar[counter].draw_power(volts=volts)
            self.__bar[counter].pack(bar_orientation=self.__orientation)
            counter=counter+1

            
    def set_box(self, pin_no):
        counter=0
        for jj in self.__bar:
            self.__bar[counter].pack_forget()
            if counter==pin_no:
                self.__bar[counter]=sd.SymbolDisplay(self.__d_frame, \
                            height=self.__LED_height, width=self.__LED_width)
                self.__bar[counter].draw_box()
            self.__bar[counter].pack(bar_orientation=self.__orientation)
            counter=counter+1

    def set_orientation(self, orientation):
        self.__orientation=orientation
        for jj in self.__bar:
            jj.pack_forget()
            jj.pack(bar_orientation=self.__orientation)


    def set_LED_orientation(self, pin_no, LED_orientation="north"):
        counter=0
        for jj in self.__bar:
            jj.pack_forget()
            if counter==pin_no:
                if isinstance(jj, ld.LEDDisplay):
                    jj=ld.LEDDisplay(self.__d_frame, \
                            height=self.__LED_height, width=self.__LED_width,\
                            LED_orientation=LED_orientation)
            jj.pack(bar_orientation=self.__orientation)
            counter=counter+1
            
                    
if __name__=="__main__":
    bar_example=tk.Tk()
    bar_widget=LEDBarDisplay(bar_example, orientation="vertical",\
                             LED_orientation="north")
    bar_widget.pack()
    bar_widget.set_one_color(led_number=2, color="purple")
    bar_widget.set_gnd(1)

  
        



