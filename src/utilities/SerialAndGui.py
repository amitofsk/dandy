#SerialAndGui is a child of tk.Tk. It is intended to be an abstract class.
#You shouldn't create objects of it. Instead, create a child class of it.
#If you do run this by itself, it opens an empty window.

#This is very similar to DigitalWithHW.py. Essentially, I'm splitting that example
#up into a parent and child class.


#Information on asyncIO came from:
#https://realpython.com/async-io-python
#Information on getting tkinter and asyncio to work together came from:
#https://stackoverflow.com/questions/47895765/use-asyncio-and-tkinter-or-another-gui-lib-together-without-freezing-the-gui-lib-together-without-freezing-the-gui-lib-together-without-freezing-the

#TODO:Clean up use of private (mangled) variables.

import asyncio
import tkinter as tk
import time
import serial
import serial.tools.list_ports as port_list
#import sys
#sys.path.append('../widgets')

#Set up PORT.
#If you are on Windows, uncomment the next line and adjust as needed.
#PORT='COM1'
#If you are on Linux, uncomment the next line and adjust as needed.
PORT='/dev/ttyACM0'
#The following lines may automatically set the port but aren't too reliable.
#ports=list(port_list.comports())
#print(ports[0].device)
#PORT=ports[0].device


class SerialAndGui(tk.Tk):
    #Here's the constructor for the DigitalWithHW class.
    #DigitalWithHW is a child of class tk.Tk, which opens a window.
    def __init__(self, loop, interval=1/20, port=PORT):
        super().__init__()
        self.__loop=loop
        self.__port=PORT
        self.protocol("WM_DELETE_WINDOW", self.close)

        
        #We have three async tasks: check_serial_data, use_serial_data
        #and updater. Each are detailed in their own function.
        self.q=asyncio.Queue()
        self.tasks=[]
        self.tasks.append(loop.create_task \
                          (self.check_serial_data(interval, self.q)))
        self.tasks.append(loop.create_task \
                          (self.use_serial_data(interval, self.q)))
        self.tasks.append(loop.create_task(self.updater(interval)))

            
    async def check_serial_data(self, interval, qIn: asyncio.Queue):
        #This async function reads data from the serial port and puts the
        #data in the queue.

        baudrate=115200
        serial_port=serial.Serial(port=self.__port, baudrate=baudrate, \
                        bytesize=8, timeout=0.1, stopbits=serial.STOPBITS_TWO)
        
        #Read a byte at a time from the serial port.
        #Convert the byte to a string, and put the string in the queue.
         
        while True:
            await asyncio.sleep(interval)
            #Read until you see the two end characters '\r\n'.
            serial_byte=serial_port.read_until('\r\n')
            #Convert the bytes read into a string
            serial_string=serial_byte.decode()
            #Slice off the two end characters
            serial_string=serial_string[:-2]
            if serial_string != "":
                await qIn.put(serial_string)
                #Uncomment the next line to see what the serial port is getting.
                #print(serial_byte)
        serial_port.close()
        

    async def use_serial_data(self, interval, qIn: asyncio.Queue):
        #This async function reads from the queue and uses the data it finds.
        #You  should really write your own version in the child class.
        while True:
            await asyncio.sleep(interval*10)
            in_string=await qIn.get()
            #print(in_string)
           

    async def updater(self, interval):
        #This async function manually updates the Tkinter GUI.
        while True:
            self.update()
            await asyncio.sleep(interval)


    def close(self):
        for task in self.tasks:
            task.cancel()
        self.__loop.stop()
        self.destroy()


if __name__=="__main__":
    loop=asyncio.get_event_loop()
    example=SerialAndGui(loop)
    loop.run_forever()
    loop.close()


        
