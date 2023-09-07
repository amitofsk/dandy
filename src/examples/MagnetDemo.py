#In this example, we use a sensor to measure 3D magnetic field, and
#we display the result on the computer using the `VectorDisplay` DANDY widget.
#
#More specifically, We use the TLE493D-W2B6 Hall effect sensor
#which measures magnetic field in the x, y, and z directions.
#This sensor will be wired to the microcontroller and will send
#data to the microcontroller using its I2C bus. The microcontroller
#will be connected to a computer by a USB cable, and it will send data
#serially to the computer down the USB cable.


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
import VectorDisplay as vd


#Set up PORT.
#If you are on Windows, uncomment the next line and adjust as needed.
PORT='COM1'
#If you are on Linux, uncomment the next line and adjust as needed.
#PORT='/dev/ttyACM0'

class MagnetDemo(sg.SerialAndGui):
     def __init__(self, loop, interval=1/20, port=PORT):
        super().__init__(loop, port=PORT)
        self.button_quit=tk.Button(self, text="Quit", \
                                   command=self.close)
        self.vector1=vd.VectorDisplay(self, height=100, width=200)

        self.vector1.pack()
        self.button_quit.pack()


     #This async function reads from the queue and uses the data it finds.
     #We're overloading the parent's version of this function.
     async def use_serial_data(self, interval, qIn: asyncio.Queue):
        while True:
            await asyncio.sleep(interval*10)
            #get the string from the queue
            in_string=await qIn.get()
            print(in_string)
            #Parse the json and pick off the element named "value"
            in_json=json.loads(in_string)
            stringX=in_json["BX"]
            valueX=float(stringX)
            stringY=in_json["BY"]
            valueY=float(stringY)
            stringZ=in_json["BZ"]
            valueZ=float(stringZ)
            #TO DO: Rescale values so they are in a good range to display.
            self.vector1.set_to_value(valueX, valueY, valueZ)
            

if __name__=="__main__":
    loop=asyncio.get_event_loop()
    example=MagnetDemo(loop)
    loop.run_forever()
    loop.close()
        

    
