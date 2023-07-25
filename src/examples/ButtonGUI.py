#This is a first example to introduce how use Tkinter.
#It is about as simple of a Tkinter example as you will find.
#When you run it, you will see a window with a label and a working quit button.

import tkinter as tk

#Define the ButtonGUI class
class ButtonGUI:
    # The function __init__ is the constructor for the class.
    def __init__(self):
        self.main_window=tk.Tk()
        self.label1=tk.Label(self.main_window, text="Welcome")
        self.button_quit=tk.Button(self.main_window, text="Quit", \
                            command=self.main_window.destroy)
        #We pack widgets to put them in the window.
        self.label1.pack()
        self.button_quit.pack()
        tk.mainloop()

# Here is our main function which creates an object of class ButtonGUI.
if __name__=="__main__":
    mygui=ButtonGUI()
