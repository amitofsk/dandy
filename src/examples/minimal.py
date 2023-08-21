##TEMPORARY, DELETE ME

import tkinter
import sys
sys.path.append('../widgets')
import VectorDisplay 

main_window=tkinter.Tk()
vec1= VectorDisplay.VectorDisplay(main_window)
vec1.set_to_value(5, 30, 25.2)
vec1.pack()
tkinter.mainloop()
