##TEMPORARY, DELETE ME

import tkinter
import sys
sys.path.append('../widgets')
import LEDBarDisplay
import SymbolDisplay

main_window=tkinter.Tk()
symbol1=SymbolDisplay.SymbolDisplay(main_window)
symbol1.draw_ground()
symbol1.pack()
#tkinter.mainloop()

