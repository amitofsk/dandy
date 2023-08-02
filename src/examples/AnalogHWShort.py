#AnalogHWShort is a child of class SerialAndGui which is a child of class Tk.


import asyncio
import tkinter as tk
import time
import json
import serial
import serial.tools.list_ports as port_list
import sys
sys.path.append('../widgets')
sys.path.append('../utilities')
import SerialAndGui as sg
import DialDisplay as dd 
import SlideDisplay as sd 
import TricolorDisplay as td
import SimplePlotDisplay as spd 


class AnalogHWShort(sg.SerialAndGui):
    #Here's the constructor.
    def __init__(self, loop, interval=1/20):
        super().__init__(loop)
        #The line above says run the parent's constructor.
        #The parent's constructor starts the three async tasks:
        #check_serial_data, use_serial_data, and updater.
        #Below, we set up the widgets for a simple GUI
        #and pack them in the window.
        
        self.button_quit=tk.Button(self, text="Quit", \
                                   command=self.close)
        self.label1=tk.Label(self, text="Hello")
        self.slide1=sd.SlideDisplay(self)
        self.dial1=dd.DialDisplay(self, \
                            height=100, width=100)

        self.tric1=td.TricolorDisplay(self, width=100, \
                            height=100)
        self.plot1=spd.SimplePlotDisplay(self)
        self.label1.pack()
        self.slide1.pack()
       
        self.dial1.pack()
        self.tric1.pack()
        self.plot1.pack()
        self.button_quit.pack()

  
    #This async function reads from the queue and uses the data it finds.
    #We're overloading the parent's version of this function.
    async def use_serial_data(self, interval, qIn: asyncio.Queue):
        while True:
            await asyncio.sleep(interval)
            #get the string from the queue
            in_string=await qIn.get()
            print(in_string)
            #Parse the json and pick off the element named "value"
            in_json=json.loads(in_string)
            val=in_json["value"]
            val_float=float(val)
            print(val)
            #Scale val so it is in a reasonable range for display
            #WHY DOES THE NEXT LINE CAUSE PROBLEMS? It is just division.
            scaled_val=val_float/10000.0
            slide_message="Value ="+str(scaled_val)
            self.label1.config(text=slide_message)
            self.dial1.set_to_value(scaled_val)
            self.slide1.set_to_value(scaled_val)
            self.tric1.set_to_value(scaled_val)
            self.plot1.add_point(scaled_val)
            

    


if __name__=="__main__":
    loop=asyncio.get_event_loop()
    example=AnalogHWShort(loop)
    loop.run_forever()
    loop.close()


