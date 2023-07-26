#This class displays a single LED to show a single digital input value.
import tkinter as tk

#TODO: d_in_canvas is still public. I should make that private (mangled).

class LEDDisplay():
    #Here's the constructor.
    def __init__(self, LED_window, height=100, width=100, color="yellow",\
                 LED_orientation="north"):
        self.__height=height
        self.__width=width
        self.__color=color
        self.__orientation=LED_orientation
        self.__bg_color="light gray"
        self.__pin_number=0
        self.d_in_canvas=tk.Canvas(LED_window, height=self.__height, \
                            width=self.__width)
        self.draw_LED(orientation=LED_orientation)


    #Here are setters and getters.
    def get_color(self):
        return self.__color

    
    def change_LED_color(self, new_color):
        self.__color=new_color
        self.draw_LED(orientation=self.__orientation)


    def get_bg_color(self):
        return self.__bg.color


    def change_bg_color(self, new_color):
        self.__bg_color=new_color
        self.d_in_canvas.create_rectangle(0,0, self.__height, self.__width,\
                fill=self.__bg_color, outline="")
        self.draw_LED(orientation=self.__orientation)


    #Note: When you resize the LED, you don't resize its window.
    #The window size is only set in the constructor.
    def set_size(self, width=100, height=100):
        #Erase the old one
        temp_color=self.__color
        self.__color=self.__bg_color
        self.draw_LED(orientation=self.__orientation)
        #Now you can draw the new one.
        self.__color=temp_color
        self.__width=width
        self.__height=height
        self.draw_LED(orientation=self.__orientation)

    
    def get_pin_number(self):
        return self.__pin_number


    def set_pin_number(self, pin_value=0):
        self.__pin_number=pin_value
        self.draw_LED(orientation=self.__orientation)


    def get_orientation(self):
        return self.__orientation

    #You have to draw in the bg color first to erase the old one.
    def set_orientation(self, LED_orientation="north"):
        #First erase the LED in the old orientation
        temp_color=self.__color
        self.__color=self.__bg_color
        self.draw_LED(orientation=self.__orientation) 
        #Now, draw LED in the new orientation.
        self.__color=temp_color
        if LED_orientation=="north":
            self.__orientation="north"
        if LED_orientation=="south":
            self.__orientation="south"
        if LED_orientation=="west":
            self.__orientation="west"
        if LED_orientation=="east":
            self.__orientation="east"
        self.draw_LED(orientation=self.__orientation)
            
    #Here are functions related to packing
    def pack(self, bar_orientation="vertical"):
        if bar_orientation=="horizontal":
            self.d_in_canvas.pack(side="right")
        else:
            self.d_in_canvas.pack()


    
    def pack_forget(self):
        self.d_in_canvas.pack_forget()


    #Here are functions related to drawing the LED in different orientations.
    def draw_LED(self, orientation="north"):
        if orientation=="north":
            self.draw_LED_north()
        elif orientation=="south":
            self.draw_LED_south()
        elif orientation=="east":
            self.draw_LED_east()
        elif orientation=="west":
            self.draw_LED_west()
        else:
            self.draw_LED_north()

    def draw_LED_north(self):
        self.LED_middle=self.d_in_canvas.create_rectangle(0.25*self.__width, \
                            0.25*self.__height, 0.75*self.__width, \
                            0.75*self.__height, fill=self.__color, \
                            outline="")
        self.LED_bottom=self.d_in_canvas.create_rectangle(0.10*self.__width, \
                            0.75*self.__height, 0.9*self.__width, \
                            0.9*self.__height, fill=self.__color, \
                            outline="")
        self.LED_top=self.d_in_canvas.create_arc(0.25*self.__width, \
                            0.05*self.__height, 0.75*self.__width, \
                            0.50*self.__height, start=0, extent=180, \
                            fill=self.__color, outline="", style="pieslice")
        if self.__pin_number>0:
            self.LED_label=self.d_in_canvas.create_text(0.5*self.__width,\
                            0.5*self.__height, fill="black", \
                            text=str(self.__pin_number)) 


    def draw_LED_south(self):
        self.LED_middle=self.d_in_canvas.create_rectangle(0.25*self.__width, \
                            0.25*self.__height, 0.75*self.__width, \
                            0.75*self.__height, fill=self.__color, \
                            outline="")
        self.LED_bottom=self.d_in_canvas.create_rectangle(0.10*self.__width, \
                            0.25*self.__height, 0.9*self.__width, \
                            0.1*self.__height, fill=self.__color, \
                            outline="")
        self.LED_top=self.d_in_canvas.create_arc(0.25*self.__width, \
                            0.50*self.__height, 0.75*self.__width, \
                            0.95*self.__height, start=180, extent=180, \
                            fill=self.__color, outline="", style="pieslice")
        if self.__pin_number>0:
            self.LED_label=self.d_in_canvas.create_text(0.5*self.__width,\
                            0.5*self.__height, fill="black", \
                            text=str(self.__pin_number)) 
        
    

    def draw_LED_east(self):
        self.LED_middle=self.d_in_canvas.create_rectangle(0.25*self.__width, \
                            0.25*self.__height, 0.75*self.__width, \
                            0.75*self.__height, fill=self.__color, \
                            outline="")
        self.LED_bottom=self.d_in_canvas.create_rectangle(0.10*self.__width, \
                            0.1*self.__height, 0.25*self.__width, \
                            0.9*self.__height, fill=self.__color, \
                            outline="")
        self.LED_top=self.d_in_canvas.create_arc(0.5*self.__width, \
                            0.25*self.__height, 0.95*self.__width, \
                            0.75*self.__height, start=270, extent=180, \
                            fill=self.__color, outline="", style="pieslice")
        if self.__pin_number>0:
            self.LED_label=self.d_in_canvas.create_text(0.5*self.__width,\
                            0.5*self.__height, fill="black", \
                            text=str(self.__pin_number)) 

    def draw_LED_west(self):
        self.LED_middle=self.d_in_canvas.create_rectangle(0.25*self.__width, \
                            0.25*self.__height, 0.75*self.__width, \
                            0.75*self.__height, fill=self.__color, \
                            outline="")
        self.LED_bottom=self.d_in_canvas.create_rectangle(0.75*self.__width, \
                            0.1*self.__height, 0.9*self.__width, \
                            0.9*self.__height, fill=self.__color, \
                            outline="")
        self.LED_top=self.d_in_canvas.create_arc(0.05*self.__width, \
                            0.25*self.__height, 0.5*self.__width, \
                            0.75*self.__height, start=90, extent=180, \
                            fill=self.__color, outline="", style="pieslice")
        if self.__pin_number>0:
            self.LED_label=self.d_in_canvas.create_text(0.5*self.__width,\
                            0.5*self.__height, fill="black", \
                            text=str(self.__pin_number)) 



    
if __name__=="__main__":
    d_in_example=tk.Tk()
    d_in_widget=LEDDisplay(d_in_example)
    d_in_widget.pack()
