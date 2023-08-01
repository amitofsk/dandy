#This class displays multiple digital inputs as an LED bar.
#When creating an object of this class, the optional parameter
# orientation can be "vertical" or "horizontal".
#LED_orientation can be "north", "south", "east", or "west".
import tkinter as tk
import sys 
sys.path.append ('../widgets') 
import LEDDisplay as ld
import SymbolDisplay as sd


class LEDBarDisplay():
    def __init__(self, bar_window, led_count=5, orientation="vertical",\
                 LED_height=50, LED_width=50, LED_orientation="north"):
        self.d_frame=tk.Frame(bar_window)
        self.bar=[]
        count=1
        for jj in range (led_count):
            self.bar=self.bar+[ld.LEDDisplay(self.d_frame, \
                        height=LED_height, width=LED_width,\
                        LED_orientation=LED_orientation)]
        for ii in self.bar:
            ii.pin_number=count
            count=count+1
            ii.pack(bar_orientation=orientation)
            ii.change_LED_color("blue")


    def pack(self):
        self.d_frame.pack()


    def set_all_color(self, color="yellow"):
        for ii in self.bar:
            ii.change_LED_color(color)


    def set_one_color(self, led_number, color="yellow"):
        #Warning here... the first LED is number 0, not 1.
        current_led=self.bar[led_number]
        current_led.change_LED_color(color)
            

if __name__=="__main__":
    bar_example=tk.Tk()
    bar_widget=LEDBarDisplay(bar_example, orientation="horizontal",\
                             LED_orientation="east")
    bar_widget.pack()
    bar_widget.set_one_color(led_number=2, color="purple")
        



