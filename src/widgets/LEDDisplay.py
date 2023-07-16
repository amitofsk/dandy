#This class displays a single LED to show a single digital input value.
import tkinter as tk

#Add member variables for shape (LED, rectangle, or circle?)

#Add functions to toggle, turn on, turn off, rotate LED 
#To clear a canvas, self.d_in_canvas.delete('all')

class LEDDisplay():
    def __init__(self, LED_window, height=100, width=100, color="yellow",\
                 LED_orientation="north"):
        self.LED_height=height
        self.LED_width=width
        self.LED_color=color
        self.bg_color="brown"
        self.pin_number=0
        self.d_in_canvas=tk.Canvas(LED_window, height=self.LED_height, \
                            width=self.LED_width)
        self.draw_LED(orientation=LED_orientation)

        
    def pack(self, bar_orientation="vertical"):
        if bar_orientation=="horizontal":
            self.d_in_canvas.pack(side="right")
        else:
            self.d_in_canvas.pack()


    def change_LED_color(self, new_color):
        self.LED_color=new_color
        self.draw_LED()


    def change_BG_color(self, new_color):
        self.bg_color=new_color
        self.d_in_canvas.create_rectangle(0,0, self.LED_height, self.LED_width,\
                fill=self.bg_color, outline="")
        self.draw_LED()


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
        self.LED_middle=self.d_in_canvas.create_rectangle(0.25*self.LED_width, \
                            0.25*self.LED_height, 0.75*self.LED_width, \
                            0.75*self.LED_height, fill=self.LED_color, \
                            outline="")
        self.LED_bottom=self.d_in_canvas.create_rectangle(0.10*self.LED_width, \
                            0.75*self.LED_height, 0.9*self.LED_width, \
                            0.9*self.LED_height, fill=self.LED_color, \
                            outline="")
        self.LED_top=self.d_in_canvas.create_arc(0.25*self.LED_width, \
                            0.05*self.LED_height, 0.75*self.LED_width, \
                            0.50*self.LED_height, start=0, extent=180, \
                            fill=self.LED_color, outline="", style="pieslice")
        if self.pin_number>0:
            self.LED_label=self.d_in_canvas.create_text(0.5*self.LED_width,\
                            0.5*self.LED_height, fill="black", \
                            text=str(self.pin_number)) 


    def draw_LED_south(self):
        self.LED_middle=self.d_in_canvas.create_rectangle(0.25*self.LED_width, \
                            0.25*self.LED_height, 0.75*self.LED_width, \
                            0.75*self.LED_height, fill=self.LED_color, \
                            outline="")
        self.LED_bottom=self.d_in_canvas.create_rectangle(0.10*self.LED_width, \
                            0.25*self.LED_height, 0.9*self.LED_width, \
                            0.1*self.LED_height, fill=self.LED_color, \
                            outline="")
        self.LED_top=self.d_in_canvas.create_arc(0.25*self.LED_width, \
                            0.50*self.LED_height, 0.75*self.LED_width, \
                            0.95*self.LED_height, start=180, extent=180, \
                            fill=self.LED_color, outline="", style="pieslice")
        if self.pin_number>0:
            self.LED_label=self.d_in_canvas.create_text(0.5*self.LED_width,\
                            0.5*self.LED_height, fill="black", \
                            text=str(self.pin_number)) 
        
    

    def draw_LED_east(self):
        self.LED_middle=self.d_in_canvas.create_rectangle(0.25*self.LED_width, \
                            0.25*self.LED_height, 0.75*self.LED_width, \
                            0.75*self.LED_height, fill=self.LED_color, \
                            outline="")
        self.LED_bottom=self.d_in_canvas.create_rectangle(0.10*self.LED_width, \
                            0.1*self.LED_height, 0.25*self.LED_width, \
                            0.9*self.LED_height, fill=self.LED_color, \
                            outline="")
        self.LED_top=self.d_in_canvas.create_arc(0.5*self.LED_width, \
                            0.25*self.LED_height, 0.95*self.LED_width, \
                            0.75*self.LED_height, start=270, extent=180, \
                            fill=self.LED_color, outline="", style="pieslice")
        if self.pin_number>0:
            self.LED_label=self.d_in_canvas.create_text(0.5*self.LED_width,\
                            0.5*self.LED_height, fill="black", \
                            text=str(self.pin_number)) 

    def draw_LED_west(self):
        self.LED_middle=self.d_in_canvas.create_rectangle(0.25*self.LED_width, \
                            0.25*self.LED_height, 0.75*self.LED_width, \
                            0.75*self.LED_height, fill=self.LED_color, \
                            outline="")
        self.LED_bottom=self.d_in_canvas.create_rectangle(0.75*self.LED_width, \
                            0.1*self.LED_height, 0.9*self.LED_width, \
                            0.9*self.LED_height, fill=self.LED_color, \
                            outline="")
        self.LED_top=self.d_in_canvas.create_arc(0.05*self.LED_width, \
                            0.25*self.LED_height, 0.5*self.LED_width, \
                            0.75*self.LED_height, start=90, extent=180, \
                            fill=self.LED_color, outline="", style="pieslice")
        if self.pin_number>0:
            self.LED_label=self.d_in_canvas.create_text(0.5*self.LED_width,\
                            0.5*self.LED_height, fill="black", \
                            text=str(self.pin_number)) 


    def pack_forget(self):
        self.d_in_canvas.pack_forget()

if __name__=="__main__":
    d_in_example=tk.Tk()
    d_in_widget=LEDDisplay(d_in_example, LED_orientation="west")
    d_in_widget.pack()
