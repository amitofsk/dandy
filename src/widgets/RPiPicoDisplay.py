#This is a child of MCDisplay specifically for drawing RPi Picos.
#Reference on RPi Pico Pinout:
# https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf
#It is 51x21mm.

#I was going to use inheritance and make this a child of a MCDisplay class.
#However, that turned out to be more effort than it was worth...too
#Much of this is specific.
#Eventually break more of this into the parent class...
#Get rid of magic number 20?
#mc_canvas should be private...
import tkinter as tk
import sys  
sys.path.append ('../widgets')  
import MCDisplay as mcd  
import LEDDisplay as ld  
import SymbolDisplay as sd  

#Get rid of magic number for LED pixel size
class RPiPicoDisplay(mcd.MCDisplay):
    def __init__(self, windowP):
        #super().__init__(windowP, left_pins=20, right_pins=20)
        self.mc_canvas=tk.Canvas(windowP, height=600, width=600)
        self.__left_pins=20
        self.__left_bar_frame=tk.Frame(windowP)
        self.__left_bar=[]
        self.__right_pins=20
        self.__right_bar_frame=tk.Frame(windowP)
        self.__right_bar=[]
        for jj in range(self.__left_pins):
            self.__left_bar=self.__left_bar+[sd.SymbolDisplay(\
                self.__left_bar_frame, height=19, width=19)]
        for jj in range(self.__right_pins):
            self.__right_bar=self.__right_bar+[sd.SymbolDisplay(\
                self.__right_bar_frame, height=19, width=19)]
        self.mc_canvas.create_window(190, 88, window=self.__left_bar_frame,\
                            anchor="nw")
        self.mc_canvas.create_window(390, 88, window=self.__right_bar_frame,\
                            anchor="nw")  

        self.redraw_body() 
                                  
        self.draw_pwr_gnd()
        #We just run tkinter update to update once.
        #We don't run tkinter in a loop here.
        windowP.update

#Rewrite next function to clean it up.
    def redraw_body(self):
        self.rect1=self.mc_canvas.create_rectangle(216, 96, 384, 504,\
                    fill="green", outline="")
        self.rect2=self.mc_canvas.create_rectangle(270,80,330,120,\
                    fill="gray", outline="")

       
    def set_led(self, pin_no):
        if(pin_no<=self.__left_pins):
            for ii in range(self.__left_pins):
                self.__left_bar[ii].pack_forget()
                if self.__left_bar[ii].pin_number==pin_no:
                    self.__left_bar[ii]=ld.LEDDisplay(self.__left_bar_frame, \
                        height=19, width=19, LED_orientation="west")
                    self.__left_bar[ii].pin_number=pin_no
            
                self.__left_bar[ii].pack()
        if(pin_no>self.__right_pins):
            for ii in range(self.__right_pins):
                self.__right_bar[ii].pack_forget()
                if self.__right_bar[ii].pin_number==pin_no:
                    self.__right_bar[ii]=ld.LEDDisplay(self.__right_bar_frame, \
                        height=19, width=19, LED_orientation="east")
                    self.__right_bar[ii].pin_number=pin_no
                self.__right_bar[ii].pack()


    def set_led_color(self, pin_no, color="pink"):
        for ii in self.__left_bar:
            if isinstance(ii,ld.LEDDisplay):
                if ii.pin_number==pin_no:                   
                    ii.change_LED_color(color)
        for ii in self.__right_bar:
            if isinstance(ii, ld.LEDDisplay):
                if ii.pin_number==pin_no:
                    ii.change_LED_color(color)

                    

    def get_led_color(self, pin_no):
        for ii in self.__left_bar:
            if isinstance(ii, ld.LEDDisplay):
                if ii.pin_number==pin_no:
                    return ii.get_color()
        for ii in self.__right_bar:
            if isinstance(ii, ld.LEDDisplay):
                if ii.pin_number==pin_no:
                    return ii.get_color()

 
#This just sets up the button. It doesn't have the button do anything.
#To have it do something, you need to bind it. 
    def set_button(self, pin_no):
        #The button has a PhotoImage of size 1x1 pixels scaled to 19x19 pixels.
        pixel=tk.PhotoImage(width=1, height=1)
        if (pin_no<=self.__left_pins):
            for ii in range(self.__left_pins):
                self.__left_bar[ii].pack_forget()
                if self.__left_bar[ii].pin_number==pin_no:
                    self.__left_bar[ii]=tk.Button(self.__left_bar_frame,\
                        image=pixel, height=19, width=19)
                      
                self.__left_bar[ii].pack()
            return self.__left_bar[pin_no-1]
        else:
            for ii in range(self.__right_pins):
                self.__right_bar[ii].pack_forget()
                if self.__right_bar[ii].pin_number==pin_no:
                    self.__right_bar[ii]=tk.Button(self.__right_bar_frame,\
                                image=pixel, height=19, width=19)
                self.__right_bar[ii].pack()
            return self.__right_bar[self.__left_pins+self.__right_pins-pin_no]


  #The next function might not be needed. 
    def get_pin_loc(self, pin_no):
        if (pin_no<=self.__left_pins):
            for ii in range(pin_no):
                pass
            return self.__left_bar[ii]
           
        else:
            for ii in range(pin_no):
                pass
            return self.__right_bar[ii-self.__left_pins+1] 
                


    def draw_pwr_gnd(self):
        #The RPiPico pins 3, 8, 13, 18, 23, 28, 33, and 38 are ground.
        #Pin 36 is 3.3V power, pin 39 is VSYS power, and pin 40 is VBUS power.
        counter=1
        for ii in self.__left_bar:
            ii.pin_number=counter
            if ((counter==3)or(counter==8)or(counter==13)or(counter==18)):
                ii.draw_ground()
            counter=counter+1
            ii.pack()
        counter=40
        for kk in self.__right_bar:
            kk.pin_number=counter
            if ((counter==23)or(counter==28)or(counter==33)or(counter==38)):
                kk.draw_ground()
            if(counter==36):
                kk.draw_power(volts=3.3)
            if(counter==39):
                kk.draw_power(volts=0)
            if(counter==40):
                kk.draw_power(volts=5.0)            
            counter=counter-1
            kk.pack()


    def pack(self):
        self.mc_canvas.pack()


    def go_button(self):
        print('button pressed.')
#OK... I can add an LED. I also may want to add a symbol (pwr or gnd).
#I also may want to add a button... which gets messier (maybe?)

if __name__=="__main__":
    rp_example=tk.Tk()
    rp_widget=RPiPicoDisplay(rp_example)
    rp_widget.pack()
    rp_widget.set_led(9)
    rp_widget.set_led_color(9, "purple")
    rp_widget.set_led(26)
    rp_widget.set_led_color(26, "purple")
    #rp_widget.set_button(10)
     
    
        

