#This example is used to test MCDisplay and all its children.

import tkinter as tk
import src.widgets.MCDisplay as mcd
import src.widgets.RPiPicoDisplay as rpp


class MCDemo:
    def __init__(self):
        self.main_window=tk.Tk()
        self.button_quit=tk.Button(self.main_window, text="Quit", \
                                   command=self.main_window.destroy)
        self.button2=tk.Button(self.main_window, text="Go",\
                               command=self.go_button)
        self.pico1=rpp.RPiPicoDisplay(self.main_window)
        self.pico1.pack()
        self.button2.pack()
        self.button_quit.pack()

        tk.mainloop()

    def go_button(self):
        print("Coming soon...")

if __name__=="__main__":
    mygui=MCDemo()
