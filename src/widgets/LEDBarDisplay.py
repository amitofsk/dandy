#This class displays multiple digital inputs as an LED bar.
import tkinter as tk
import LEDDisplay

#Add memeber variables for on_color, off_color, height, width, orientation,
#number of LEDs, 
#Use an array here? with late binding, define length at compile time?
#Let's start simpler, with an array of 3 LEDs, and work the way up...
#Try using a tuple of LEDDisplays

class LEDBarDisplay():
    def __init__(self, bar_window, led_count=5, orientation="vertical",\
                 LED_height=50, LED_width=50):
        self.d_frame=tk.Frame(bar_window)
        self.bar=[]        
        for jj in range (led_count):
            self.bar=self.bar+[LEDDisplay.LEDDisplay(self.d_frame, \
                        height=LED_height, width=LED_width)]
        for ii in self.bar:
            ii.pack(LED_orientation=orientation)
            ii.change_LED_color("pink")


    def pack(self):
        self.d_frame.pack()


    def set_color_all(self):
        for ii in self.bar:
            ii.change_LED_color("yellow")


    def set_color_one(self, led_number):
        #Warning here... the first LED is number 0, not 1.
        current_led=self.bar[led_number]
        current_led.change_LED_color("red")
            

if __name__=="__main__":
    bar_example=tk.Tk()
    bar_widget=LEDBarDisplay(bar_example, orientation="hx")
    bar_widget.pack()
        



