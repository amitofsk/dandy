##TEMPORARY, DELETE ME

import tkinter
import sys
sys.path.append('../widgets')
import LEDBarDisplay


main_window=tkinter.Tk()
bar1=LEDBarDisplay.LEDBarDisplay(main_window)
bar1.set_all_color("yellow")
bar1.pack()
#tkinter.mainloop()

