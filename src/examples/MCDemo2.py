#OK... trying to get the RPiPico widget working with the asyncio example...

import asyncio
import tkinter as tk
import time
import serial
import src.widgets.MCDisplay as mcd
import src.widgets.RPiPicoDisplay as rpp


#Wire up a button to pin 9
BUTTON_NO=9

class MCDemo2(tk.Tk):
    def __init__(self, loop, interval=1/40):
        super().__init__()
        self.loop=loop
        self.protocol=("WM_DELETE_WINDOW", self.close)
        self.q=asyncio.Queue()
        self.tasks=[]
        self.tasks.append(loop.create_task(self.checkdigin(1/20,self.q)))
        self.tasks.append(loop.create_task(self.consumeQueue(1/20, self.q)))
        self.tasks.append(loop.create_task(self.updater(interval)))
        self.digBit=1
        self.button_quit=tk.Button(self, text="Quit", command=self.close)
        self.pico1=rpp.RPiPicoDisplay(self)
        self.pico1.pack()
        self.button_quit.pack()

    async def checkdigin(self, interval, qIn:asyncio.Queue):
        #Next line is linux specific. See asyncPractice4.py
        port="/dev/ttyACM0"
        baudrate=115200
        serialPort=serial.Serial(port=port, baudrate=baudrate,\
                        bytesize=8, timeout=0.1, stopbits=serial.STOPBITS_TWO)
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
        print("Hey")
        while True:
            await asyncio.sleep(interval)
            i=await qIn.get()
            intval=int.from_bytes(i, "big")
            if intval==84:
                print("Found T")
                self.pico1.change_left_led_color(BUTTON_NO, "green")
                
            if intval==70:
                print("Found F")
                self.pico1.change_left_led_color(BUTTON_NO, "blue")


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
        
        
