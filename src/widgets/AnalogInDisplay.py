#This is a parent class of widgets used for displaying analog input.
#Should this be abstract?
#I recommend using the child classes instead.

import tkinter as tk



class AnalogInDisplay:
    def __init__(self, aInWindow):
        self.minimum=0.0
        self.maximum=10.0
        #Test what happens if aInHeight and aInWidth vary and if they are unequal.
        self.aInHeight=100
        self.aInWidth=100
        self.aInValue=0.0
        self.aInCanvas=tk.Canvas(aInWindow, height=self.aInHeight, width=self.aInWidth)
        #self.aInLabel=tk.Label(aInWindow, text=str(self.aInValue))

        #self.aInLabel.pack()
        #self.pack()


    
    #New constructor scalable to different sizes?

    #I'm writing the next function so that syntax is closer to syntax
    #of preexisting tkinter widgets. Yes, it seems a bit silly to have
    #such a short function, but there is a reason.
    def pack(self):
        self.aInCanvas.pack()    




#When you run main, you should get a blank window. This class is really supposed to be
    #abstract. You really should only use its children.
if __name__=="__main__":
    analogInWidget=tk.Tk()
    analogInWidget=AnalogInDisplay(analogInWidget)
    analogInWidget.pack()
