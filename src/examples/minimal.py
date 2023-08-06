import tkinter
import sys
sys.path.append('../widgets')
import LEDDisplay 

main_window=tkinter.Tk()
led1= LEDDisplay.LEDDisplay(main_window)
led1.change_LED_color("purple")
led1.set_orientation("east")
led1.pack()
tkinter.mainloop()
