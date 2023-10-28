#This example has a potentiometer wired to a Raspberry Pi Pico.
#It has a second potentiometer wired to an Arduino. Both microcontrollers
#send data, via USB cables, to a computer.
#Information is displayed in a DialDisplay widget for each microcontroller. 

#Set up your ports. 
#If you are on Windows, uncomment the next lines and adjust as needed.
PORTA='COM1'
PORTB='COM2'
#If you are on Linux, uncomment the next lines and adjust as needed.
#PORTA='/dev/ttyACM0'
#PORTB='/dev/ttyACM1'

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

class TwoMC(tk.Tk):
    def __init__(self, loop, interval=1/20):
        super().__init__()
        self.__loop=loop
        self.__portA=PORTA
        self.__portB=PORTB
        self.protocol("WM_DELETE_WINDOW", self.close)

        
        #We have four async tasks: check_serial_dataA,
        #check_serial_dataB, and use_serial_data
        #and updater. Each are detailed in their own function.
        self.q=asyncio.Queue()
        self.tasks=[]
        self.tasks.append(loop.create_task \
                          (self.check_serial_dataA(interval, self.q)))
        self.tasks.append(loop.create_task \
                          (self.check_serial_dataB(interval, self.q)))
        self.tasks.append(loop.create_task \
                          (self.use_serial_data(interval, self.q)))
        self.tasks.append(loop.create_task(self.updater(interval)))
        self.button_quit=tk.Button(self, text="Quit", \
                                   command=self.close)
        self.dial1=dd.DialDisplay(self, height=100, width=100)
        self.dial2=dd.DialDisplay(self, height=100, width=100)
        self.dial1.pack()
        self.dial2.pack()
        self.button_quit.pack()



    async def use_serial_data(self, interval, qIn: asyncio.Queue):
        while True:
            await asyncio.sleep(interval)
            #get the string from the queue
            in_string=await qIn.get()
            print(in_string)
            #Parse the json and pick off the element named "value"
            in_json=json.loads(in_string)
            
            board_read=in_json["boardNumber"]
            print(board_read)
            val=in_json["value"]
            val_float=float(val)
            if(board_read=="1"):
                scaled_value=val_float/6000
                self.dial1.set_to_value(scaled_value)
            else:
                scaled_value=val_float/1024
                self.dial2.set_to_value(scaled_value)


    async def check_serial_dataA(self, interval, qIn: asyncio.Queue):
        #This async function reads data from the serial port and puts the
        #data in the queue.

        baudrate=115200
        serial_port=serial.Serial(port=self.__portA, baudrate=baudrate, \
                        bytesize=8, timeout=0.1, stopbits=serial.STOPBITS_TWO)
        
        #Read a byte at a time from the serial port.
        #Convert the byte to a string, and put the string in the queue.
        print('checking A')
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
        




    async def check_serial_dataB(self, interval, qIn: asyncio.Queue):
        #This async function reads data from the serial port and puts the
        #data in the queue.

        baudrate=115200
        serial_port=serial.Serial(port=self.__portB, baudrate=baudrate, \
                        bytesize=8, timeout=0.1, stopbits=serial.STOPBITS_TWO)
        
        #Read a byte at a time from the serial port.
        #Convert the byte to a string, and put the string in the queue.
        print('checking B')
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
    example=TwoMC(loop)
    loop.run_forever()
    loop.close()
