import tkinter as tk
import sys
sys.path.append('../widgets')
import LEDDisplay as ld

class DigitalNoHW:
    def __init__(self):
        self.main_window=tk.Tk()
        self.button_quit=tk.Button(self.main_window, text="Quit", \
                            command=self.main_window.destroy)
        self.button2=tk.Button(self.main_window, text="Toggle", \
                               command=self.getValue)
        self.led1=ld.LEDDisplay(self.main_window)
        self.button_quit.pack()
        self.button2.pack()
        self.led1.pack()
        tk.mainloop()

    def getValue(self):
        if(self.led1.get_color()=="yellow"):
            self.led1.change_LED_color("blue")
        elif (self.led1.get_color()=="blue"):
            self.led1.change_LED_color("yellow")

if __name__=="__main__":
    mygui=DigitalNoHW()
