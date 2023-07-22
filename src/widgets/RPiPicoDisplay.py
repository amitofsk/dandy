#This is a child of MCDisplay specifically for drawing RPi Picos.
#Reference on RPi Pico Pinout:
# https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf
#It is 51x21mm.

import tkinter as tk
import src.widgets.MCDisplay as mcd
import src.widgets.LEDDisplay as ld
import src.widgets.SymbolDisplay as sd


class RPiPicoDisplay(mcd.MCDisplay):
    def __init__(self, windowP):
        super().__init__(windowP)
        self.redraw_body()

        self.left_bar_frame=tk.Frame(windowP)
        self.left_bar=[]
        self.right_bar_frame=tk.Frame(windowP)
        self.right_bar=[]
        self.left_window=self.mc_canvas.create_window(190, 88, window=self.left_bar_frame,\
                            anchor="nw")
        self.mc_canvas.create_window(390, 88, window=self.right_bar_frame,\
                            anchor="nw")
                                     
        for jj in range(20):
            self.left_bar=self.left_bar+[sd.SymbolDisplay(self.left_bar_frame, \
                            height=19, width=19)]
            self.right_bar=self.right_bar+[sd.SymbolDisplay(self.right_bar_frame,\
                            height=19, width=19)]
        counter=1
        for ii in self.left_bar:
            ii.pin_number=counter
            if ((counter==3)or(counter==8)or(counter==13)or(counter==18)):
                ii.draw_ground()
            counter=counter+1
            ii.pack()
        counter=40
        for kk in self.right_bar:
            kk.pin_number=counter
            counter=counter-1
            kk.pack()
       
        self.set_left_led(9)
        
        self.change_left_led_color(9, "pink")
        
        windowP.update


    def redraw_body(self):
        self.mc_canvas.delete(self.rect1)
        self.mc_canvas.delete(self.rect2)
        self.rect1=self.mc_canvas.create_rectangle(216, 96, 384, 504,\
                    fill="green", outline="")
        self.rect2=self.mc_canvas.create_rectangle(270,80,330,120,\
                    fill="gray", outline="")

        
    def set_left_led(self, pin_no):
        for ii in range(len(self.left_bar)):
            self.left_bar[ii].pack_forget()
            if self.left_bar[ii].pin_number==pin_no:
                self.left_bar[ii]=ld.LEDDisplay(self.left_bar_frame, \
                    height=19, width=19, LED_orientation="west")
                self.left_bar[ii].pin_number=pin_no
                self.left_bar[ii].pack()
            else:
                self.left_bar[ii].pack()


    def change_left_led_color(self, pin_no, color="pink"):
        
        for ii in self.left_bar:
            if isinstance(ii,ld.LEDDisplay):
                if ii.pin_number==pin_no:
                    
                    ii.change_LED_color(color)
        
                  

if __name__=="__main__":
    rp_example=tk.Tk()
    rp_widget=RPiPicoDisplay(rp_example)
    rp_widget.pack()
