
#This class displays a picture of a microcontroller. The pins can be
#replaced by LEDs, buttons, or other widgets.
#This class has multiple children that draw specific
#microcontrollers. See RPiPicoDisplay.py, AUnoDisplay.py, ANanoEveryDisplay.py,
#and AMKRDisplay.py.


import tkinter as tk
import sys
sys.path.append ('../widgets')
import LEDDisplay as ld  
import SymbolDisplay as sd  
import SlideDisplay as sld
import TricolorDisplay as td
import DialDisplay as dd

class MCDisplay:
    def __init__(self, windowMC, leftPins=15, rightPins=15, widgetSize=21):
        self.mc_canvas=tk.Canvas(windowMC, height=600, width=600)


        #Set up some parameters specific to the microcontroller
        self.__left_pins=leftPins
        self.__right_pins=rightPins
        self.__widget_size=widgetSize

        #Set up the left_bar and right_bar of widgets for the rows of pins.
        self.__left_bar_frame=tk.Frame(windowMC)
        self.__right_bar_frame=tk.Frame(windowMC)
        self.__left_bar=[]
        self.__right_bar=[]
        for jj in range(self.__left_pins):
            self.__left_bar=self.__left_bar+[sd.SymbolDisplay(\
                 self.get_left_bar_frame(), height=self.__widget_size, \
                width=self.__widget_size)]
        for jj in range(self.__right_pins):
            self.__right_bar=self.__right_bar+[sd.SymbolDisplay(\
                self.get_right_bar_frame(), height=self.__widget_size, \
                width=self.__widget_size)]
        for jj in range(self.__left_pins):
            self.__left_bar[jj].pack()
        for jj in range(self.__right_pins):
            self.__right_bar[jj].pack()
            
        self.redraw_body()
        #We don't run tkinter in a loop. Instead, we just updat it once.
        windowMC.update()


    #Here are the setters and getters for left_pins, right_pins, and widget_size
    #I need getters for left_pins, right_pins, and widget_size as well
    #as a setter for widget_size?
    def get_left_pins(self):
        return self.__left_pins


    def get_right_pins(self):
        return self.__right_pins


    def get_widget_size(self):
        return self.__widget_size


    def set_widget_size(self, widgetSize):
        self.__widget_size=widgetSize
        return self.__widget_size

    #Here are setters and getters for left_bar and right_bar, left_bar_frame,
    #and right_bar_frame
    def get_left_bar_frame(self):
        return self.__left_bar_frame


    def get_right_bar_frame(self):
        return self.__right_bar_frame

    def get_left_bar(self):
        return self.__left_bar

    def get_right_bar(self):
        return self.__right_bar
    
    #Here are the other setters and getters
    def set_led_color(self, pin_no, color="yellow"):
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


    def set_led(self, pin_no):
        if(pin_no<=self.__left_pins):
            for ii in range(self.__left_pins):
                self.__left_bar[ii].pack_forget()
                if self.__left_bar[ii].pin_number==pin_no:
                    self.__left_bar[ii]=ld.LEDDisplay(self.get_left_bar_frame(), \
                        height=self.__widget_size, width=self.__widget_size, \
                        LED_orientation="west")
                    self.__left_bar[ii].pin_number=pin_no
                self.__left_bar[ii].pack()
        if(pin_no>self.__right_pins):
            for ii in range(self.__right_pins):
                self.__right_bar[ii].pack_forget()
                if self.__right_bar[ii].pin_number==pin_no:
                    self.__right_bar[ii]=ld.LEDDisplay(self.get_right_bar_frame(), \
                        height=self.__widget_size, width=self.__widget_size, \
                        LED_orientation="east")
                    self.__right_bar[ii].pin_number=pin_no
                self.__right_bar[ii].pack()



    def set_button(self, pin_no):
        #This just sets up the button. It doesn't have the button do anything.
        #To have it do something, you need to bind it. 
        #The button has a PhotoImage of size 1x1 pixels scaled to
        #widget_size x widget_size pixels.
        pixel=tk.PhotoImage(width=1, height=1)
        if (pin_no<=self.__left_pins):
            for ii in range(self.__left_pins):
                self.__left_bar[ii].pack_forget()
                if self.__left_bar[ii].pin_number==pin_no:
                    self.__left_bar[ii]=tk.Button(self.get_left_bar_frame(),\
                        image=pixel, height=self.__widget_size, \
                        width=self.__widget_size)
                      
                self.__left_bar[ii].pack()
            return self.__left_bar[pin_no-1]
        else:
            for ii in range(self.__right_pins):
                self.__right_bar[ii].pack_forget()
                if self.__right_bar[ii].pin_number==pin_no:
                    self.__right_bar[ii]=tk.Button(self.get_right_bar_frame(),\
                                image=pixel, height=self.__widget_size,\
                                width=self.__widget_size)
                self.__right_bar[ii].pack()
            return self.__right_bar[self.__left_pins+self.__right_pins-pin_no]


    def set_tricolor(self, pin_no):
        if(pin_no<=self.__left_pins):
            for ii in range(self.__left_pins):
                self.__left_bar[ii].pack_forget()
                if self.__left_bar[ii].pin_number==pin_no:
                    self.__left_bar[ii]=td.TricolorDisplay(self.get_left_bar_frame(), \
                        height=self.__widget_size, width=self.__widget_size)
                    self.__left_bar[ii].pin_number=pin_no
                self.__left_bar[ii].pack()
        if(pin_no>self.__right_pins):
            for ii in range(self.__right_pins):
                self.__right_bar[ii].pack_forget()
                if self.__right_bar[ii].pin_number==pin_no:
                    self.__right_bar[ii]=td.TricolorDisplay(self.get_right_bar_frame(), \
                        height=self.__widget_size, width=self.__widget_size)
                    self.__right_bar[ii].pin_number=pin_no
                self.__right_bar[ii].pack()


    def set_dial(self, pin_no):
        if(pin_no<=self.__left_pins):
            for ii in range(self.__left_pins):
                self.__left_bar[ii].pack_forget()
                if self.__left_bar[ii].pin_number==pin_no:
                    self.__left_bar[ii]=dd.DialDisplay(self.get_left_bar_frame(), \
                        height=self.__widget_size, width=self.__widget_size)
                    self.__left_bar[ii].pin_number=pin_no
                self.__left_bar[ii].pack()
        if(pin_no>self.__right_pins):
            for ii in range(self.__right_pins):
                self.__right_bar[ii].pack_forget()
                if self.__right_bar[ii].pin_number==pin_no:
                    self.__right_bar[ii]=dd.DialDisplay(self.get_right_bar_frame(), \
                        height=self.__widget_size, width=self.__widget_size)
                    self.__right_bar[ii].pin_number=pin_no
                self.__right_bar[ii].pack()


    def set_slide(self, pin_no):
        if(pin_no<=self.__left_pins):
            for ii in range(self.__left_pins):
                self.__left_bar[ii].pack_forget()
                if self.__left_bar[ii].pin_number==pin_no:
                    self.__left_bar[ii]=sld.SlideDisplay(self.get_left_bar_frame(), \
                        height=self.__widget_size, width=self.__widget_size)
                    self.__left_bar[ii].pin_number=pin_no
                self.__left_bar[ii].pack()
        if(pin_no>self.__right_pins):
            for ii in range(self.__right_pins):
                self.__right_bar[ii].pack_forget()
                if self.__right_bar[ii].pin_number==pin_no:
                    self.__right_bar[ii]=sld.SlideDisplay(self.get_right_bar_frame(), \
                        height=self.__widget_size, width=self.__widget_size)
                    self.__right_bar[ii].pin_number=pin_no
                self.__right_bar[ii].pack()
      
    def get_pin_loc(self, pin_no):
        if (pin_no<=self.__left_pins):
            for ii in range(pin_no):
                pass
            return self.__left_bar[ii]
        else:
            for ii in range(pin_no):
                pass
            return self.__right_bar[ii-self.__left_pins+1] 
                

    #Here are the functions related to drawing widgets
    def redraw_body(self):
        self.mc_canvas.create_window(190, 88, window=self.get_left_bar_frame(),\
                            anchor="nw")
        self.mc_canvas.create_window(390, 88, window=self.get_right_bar_frame(),\
                        anchor="nw")
        self.rect1=self.mc_canvas.create_rectangle(220,50, 380,350, fill="green",\
                       outline="")
        self.rect2=self.mc_canvas.create_rectangle(290, 40, 320, 70, \
                        fill="gray", outline="")


    def draw_pwr_gnd(self):
        #This function sets pin numbers too.
        #In child versions, this function sets power and gnd symbols too.
        counter=1
        for ii in self.get_left_bar():
            ii.pin_number=counter
            counter=counter+1
            ii.pack()
        counter=self.__left_pins+self.__right_pins
        for kk in self.get_right_bar():
            counter=counter-1
            kk.pack()


    #Here are functions related to packing.
    def pack(self):
        self.mc_canvas.pack()


    def pack_forget(self):
        self.mc_canvas.pack_forget()


if __name__=="__main__":
    mc_example=tk.Tk()
    mc_widget=MCDisplay(mc_example)
    mc_widget.pack()
        
        

        
