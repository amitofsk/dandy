#When you run this example, you will see a quit button and a second button.
#When you press that button, the computer sends the character 'Z' to the
#microcontroller. Make sure to set your port correctly.

import asyncio
import tkinter as tk
import time
import serial
import serial.tools.list_ports as port_list
import sys

#If you are on Windows, uncomment the next line and adjust as needed.
#port='COM1'
#If you are on Linux, uncomment the next line and adjust as needed.
PORT='/dev/ttyACM0'

class DigitalOutDisplay(tk.Tk):
    def __init__(self):
        super().__init__()
        self.button1= tk.Button(self, text="toggle", \
                               command= self.toggle_me)
        self.button_quit=tk.Button(self, text="Quit", command=self.destroy)
        self.button1.pack()
        self.button_quit.pack()

        baudrate=115200
        self.serial_port=serial.Serial(port=PORT, baudrate=baudrate, \
                        bytesize=8, timeout=0.1, stopbits=serial.STOPBITS_TWO)
        
        tk.mainloop()


    def toggle_me(self):
        out_string='Z'
        print('I wrote Z')
        #The function bytes casts a string to bytes.
        self.serial_port.write(bytes(out_string,'utf-8'))

if __name__=="__main__":
    mygui=DigitalOutDisplay()
    
        
                                   
