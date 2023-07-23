
#Read the instructions in Dandy.md. 
#Before running this program, upload the serialRead.py to your microcontroller.
#When this runs, you will see a small icon and a quit button.
#When you press the pushbutton on the circuit connected to the microcontroller, 
#the small icon will change.

#Information on asyncIO came from:
#https://realpython.com/async-io-python
#Information on getting tkinter and asyncio to work together came from:
#https://stackoverflow.com/questions/47895765/use-asyncio-and-tkinter-or-another-gui-lib-together-without-freezing-the-gui-lib-together-without-freezing-the-gui-lib-together-without-freezing-the


import asyncio
import tkinter as tk
import itertools as it
import time
import serial
import serial.tools.list_ports as port_list

class DigDisplay(tk.Tk):
    #Here's the constructor for the class DigDisplay.
    #This is a child of tk.Tk which opens a window.
    def __init__(self, loop, interval=1/40):
        super().__init__()
        self.loop=loop
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.q=asyncio.Queue()
        self.tasks=[]
        #We'll have three async tasks, named checkdigin, consumeQueue, and updater.
        #Each of these are detailed in their own function.
        self.tasks.append(loop.create_task(self.checkdigin(1/20,self.q)))
        self.tasks.append(loop.create_task(self.consumeQueue(1/20, self.q)))
        self.tasks.append(loop.create_task(self.updater(interval)))
        #Set up the widgets and pack them into the window.
        self.digBit=1
        self.buttonQuit=tk.Button(self, text="Quit", command=self.close)
        self.smileOn=tk.PhotoImage(file='./smileOn.png')
        self.smileOff=tk.PhotoImage(file='./smileOff.png')
        self.label1=tk.Label(self, image=self.smileOn)
        self.label1.pack()
        self.buttonQuit.pack()


    async def checkdigin(self, interval, qIn:asyncio.Queue):
        #This asyncio function reads from the serial port and writes to the queue if it finds T or F.
        ports=list(port_list.comports())
        print(ports[0].device)
        port=ports[0].device
        #If you are on windows and you get an error saying it can't find the port, try the line below.
        #port='COM6'
        #If you are on linux and you get an error saying it can't find the port, try the line below.
        #port='/dev/ttyACM0'
        baudrate=115200
        serialPort=serial.Serial(port=port, baudrate=baudrate, bytesize=8, timeout=0.1, stopbits=serial.STOPBITS_TWO)
        imax=10000
        for ii in range(imax):
            await asyncio.sleep(interval)
            serialByte=serialPort.read()
            serialInt=int.from_bytes(serialByte, "big")
            if serialInt != 0:
                await qIn.put(serialByte)
                print(serialByte)
        serialPort.close()
        

    async def consumeQueue(self, interval, qIn: asyncio.Queue):
        #This asyncio function reads from the queue and sets the appropriate picture if necessary
        while True:
            await asyncio.sleep(interval)
            i=await qIn.get()
            #The character T has ascii value 84. The character F has 
            #ascii value 70. We're actually reading in individual bytes.
            #The next line converts bytes to integers.
            intval=int.from_bytes(i, "big")
            print(intval)
            if intval==84:
                print("Found T")
                self.label1.configure(image=self.smileOn)
            if intval==70:
                print("Found F")
                self.label1.configure(image=self.smileOff)
                


    async def updater(self, interval):
        #This async function manually updates the tkinter GUI.
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
    
