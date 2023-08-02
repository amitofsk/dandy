#Here's the long version.

import asyncio
import tkinter as tk
import sys  
sys.path.append('../widgets') 
import time
import serial
import MCDisplay as mcd  
import RPiPicoDisplay as rpp  

#Button is wired to pin 21
BUTTON_NO=21

class MCDemo2(tk.Tk):
    def __init__(self, loop, interval=1/40):
        super().__init__()
        self.loop=loop
        self.protocol=("WM_DELETE_WINDOW", self.close)
        self.q=asyncio.Queue()
        self.tasks=[]
        self.tasks.append(loop.create_task \
                          (self.check_serial_data(interval, self.q)))
        self.tasks.append(loop.create_task \
                          (self.use_serial_data(interval, self.q)))
        self.tasks.append(loop.create_task(self.updater(interval)))

        self.button_quit=tk.Button(self, text="Quit", command=self.close)
        self.mc1=rpp.RPiPicoDisplay(self)
        self.mc1.set_led(BUTTON_NO)
        self.mc1.pack()
        self.button_quit.pack()

    async def check_serial_data(self, interval, qIn: asyncio.Queue):
        print('check_serial_data running')
         #This async function reads data from the serial port and puts the
        #data in the queue.

        #Set up to read from the serial port.
        #ports=list(port_list.comports())
        #print(ports[0].device)
        #port=ports[0].device
        #If you are on windows and you get an error saying it can't find the port, try the line below.
        #port='COM6'
        #If you are on linux and you get an error saying it can't find the port, try the line below.
        port='/dev/ttyACM0'
        baudrate=115200
        serial_port=serial.Serial(port=port, baudrate=baudrate, bytesize=8, timeout=0.1, stopbits=serial.STOPBITS_TWO)
        
        #Read a byte at a time from the serial port.
        #Convert the byte to a string, and put the string in the queue.
        
        #TODO: Move setting port to very top...That step is needed.
        #In linux, I had to set port manually here.
        while True:
            await asyncio.sleep(interval)
            serial_byte=serial_port.read()
            serial_string=serial_byte.decode()
            print(serial_byte)
            if serial_string != "":
                await qIn.put(serial_string)
                #Uncomment the next line to see what the serial port is getting.
                #print(serial_byte)
        serial_port.close()


    async def use_serial_data(self, interval, qIn: asyncio.Queue):
        #This async function reads from the queue and uses the data it finds.
        while True:
            await asyncio.sleep(interval)
            in_string=await qIn.get()
            if in_string=="T":
                print("T")
                self.mc1.set_led_color(BUTTON_NO, "yellow")
            if in_string=="F":
                print("F")
                self.mc1.set_led_color(BUTTON_NO, "blue")  
 

    async def updater(self, interval):
        while True:
            self.update()
            await asyncio.sleep(interval)


    def close(self):
        for task in self.tasks:
            task.cancel()
            self.loop.stop()
            self.destroy()
                



if __name__=="__main__":
    loop=asyncio.get_event_loop()
    app=MCDemo2(loop)
    loop.run_forever()
    loop.close()
        
        
