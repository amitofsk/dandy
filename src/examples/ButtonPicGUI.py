#This is a second example to introduce Tkinter.
#When you run it, you will see a window with two buttons and a label containing
#a PhotoImage. When you press the button, you toggle the image.

import tkinter as tk

class ButtonPicGUI:
    def __init__(self):
        self.main_window=tk.Tk()
        self.smileOn=tk.PhotoImage(file='./smileOn.png')
        self.smileOff=tk.PhotoImage(file='./smileOff.png')
        self.image_number=0

        #This label contains a PhotoImage instead of text.
        self.label1=tk.Label(self.main_window, image=self.smileOn)
        #When button1 is pressed, the instructions in the function
        #toggle_me are followed. We define this function below.
        self.button1=tk.Button(self.main_window, text="Press Me", \
                               command=self.toggle_me)
        self.button_quit=tk.Button(self.main_window, text="Quit", \
                                   command=self.main_window.destroy)

        self.label1.pack()
        self.button1.pack()
        self.button_quit.pack()

        tk.mainloop()

        
    #Here we define the toggle_me function
    def toggle_me(self):
        if self.image_number==0:
            self.label1.configure(image=self.smileOff)
            self.image_number=1
        else:
            self.label1.configure(image=self.smileOn)
            self.image_number=0


if __name__=="__main__":
    mygui=ButtonPicGUI()
