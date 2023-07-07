#Ok... goal of this one... Circuit python code will check a digital input, button.
#If the input state is changed (with debounce?), it will send a message on
#the serial bus.
#This code, will use asyncio and tkinter and a queue. If it receives a change
#of state, it will change the smiley between yellow and gray.

#Reference used to get tkinter and asyncio to work together
#https://stackoverflow.com/questions/47895765/use-asyncio-and-tkinter-or-another-gui-lib-together-without-freezing-the-gui

#Notice the use of update here...


import asyncio
import tkinter as tk
import itertools as it
import time
import serial
import serial.tools.list_ports as port_list

class DigDisplay(tk.Tk):
    def __init__(self, loop, interval=1/40):
        super().__init__()
        #self.widget=tk.Tk()
        self.loop=loop
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.q=asyncio.Queue()
        self.tasks=[]
        self.tasks.append(loop.create_task(self.checkdigin(1/20,self.q)))
        self.tasks.append(loop.create_task(self.consumeQueue(1/20, self.q)))
        self.tasks.append(loop.create_task(self.updater(interval)))
        self.digBit=1
        self.buttonQuit=tk.Button(self, text="Quit", command=self.close)
        self.smileOn=tk.PhotoImage(file='pics/smileOn.png')
        self.smileOff=tk.PhotoImage(file='pics/smileOff.png')
        self.label1=tk.Label(self, image=self.smileOn)
        self.label1.pack()
        self.buttonQuit.pack()


    async def checkdigin(self, interval, qIn:asyncio.Queue):
        #This asyncio function reads from the serial port and writes to the queue if it finds T or F.
        print("Yo")
        #Change the next line depending on your setup.
        #On a windows machine it might be something like.
        #port='COM1'
        #You should be able to figure it out using something like ...
        #ports=list(port_list.comports())
        #print(ports[0].device)
        #port=ports[0].device
        port='/dev/ttyACM0'
        baudrate=115200
        serialPort=serial.Serial(port=port, baudrate=baudrate, bytesize=8, timeout=0.1, stopbits=serial.STOPBITS_TWO)
        imax=10000
        for ii in range(imax):
            await asyncio.sleep(interval)
            #serialByte=await serialPort.read()
            serialByte=serialPort.read()
            #print(serialByte)
            serialInt=int.from_bytes(serialByte, "big")
            if serialInt != 0:
                #t=time.perf_counter()
                await qIn.put(serialByte)
                print(serialByte)
        serialPort.close()
        

    async def consumeQueue(self, interval, qIn: asyncio.Queue):
        #This asyncio function reads from the queue and sets the appropriate picture if necessary
        print("hi")
        while True:
            await asyncio.sleep(interval)
            i=await qIn.get()
            intval=int.from_bytes(i, "big")
            print(intval)
            if intval==84:
                print("Found T")
                self.label1.configure(image=self.smileOn)
            if intval==70:
                print("Found F")
                self.label1.configure(image=self.smileOff)
                


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
    app=DigDisplay(loop)
    loop.run_forever()
    loop.close()
    
