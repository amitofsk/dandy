#See the tutorial for more details. Before you run this, you should connect
#a pushbutton to your microcontroller, and you should run
# microcontr/serialWriteMP.py on your microcontroller. When you run this,
#you will see a LEDDisplay widget and a quit button. When you hold
#down the pushbuntton wired to the microcontroller, the LEDDisplay widget's
#color will change.

#Information on asyncIO came from:
#https://realpython.com/async-io-python
#Information on getting tkinter and asyncio to work together came from:
#https://stackoverflow.com/questions/47895765/use-asyncio-and-tkinter-or-another-gui-lib-together-without-freezing-the-gui-lib-together-without-freezing-the-gui-lib-together-without-freezing-the

   #2026 references
    #https://docs.python.org/3/library/asyncio-task.html#coroutine
    #Ref: https://stackoverflow.com/questions/58774718/asyncio-in-corroutine-runtimeerror-no-running-event-loop
    #https://bobbyhadz.com/blog/deprecationwarning-there-is-no-current-event-loop
    #https://stackoverflow.com/questions/34710835/proper-way-to-shutdown-asyncio-tasks







import asyncio
import tkinter as tk
import time
import serial
import serial.tools.list_ports as port_list
import sys
sys.path.append('../widgets')
import LEDDisplay as ld

#Set up PORT.
#If you are on Windows, uncomment the next line and adjust as needed.
#PORT='COM1'
#If you are on Linux, uncomment the next line and adjust as needed.
PORT='/dev/ttyACM0'


class DigitalHWLong(tk.Tk):
    #Here's the constructor for the DigitalWithHW class.
    #DigitalWithHW is a child of class tk.Tk, which opens a window.
    def __init__(self,  interval=1/20):
        super().__init__()
        self.loop=asyncio.new_event_loop()
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.q=asyncio.Queue()
        self.interval=interval
       


        #Set up the widgets for a simple GUI and pack them in the window.
        self.led1=ld.LEDDisplay(self)
        self.button_quit=tk.Button(self, text="Quit", \
                                   command=self.close)
        self.led1.pack()
        self.button_quit.pack()
        
        #Notice that we don't start Tkinter's main loop here. Instead
        #the function updater will update the GUI.

    async def taskSetup():
        #First, we actually call the constructor to set up the GUI.
        #Then, we start our three tasks. The tasks are: check_serial_data, use_serial_data
        #and updater. Each are detailed in their own function.
        setupObj=DigitalHWLong()
        async with asyncio.TaskGroup() as tg:
            task1=tg.create_task(setupObj.check_serial_data(setupObj.interval, setupObj.q))
            task2=tg.create_task(setupObj.use_serial_data(setupObj.interval, setupObj.q))
            task3=tg.create_task(setupObj.updater(setupObj.interval))
         
        
    async def check_serial_data(self, interval, qIn: asyncio.Queue):
        #This async function reads data from the serial port and puts the
        #data in the queue.

        #Set up to read from the serial port.
        baudrate=115200
        serial_port=serial.Serial(port=PORT, baudrate=baudrate, \
                        bytesize=8, timeout=0.1, stopbits=serial.STOPBITS_TWO)
        
        #Read a byte at a time from the serial port.
        #Convert the byte to a string, and put the string in the queue.
        while True:
            await asyncio.sleep(interval)
            serial_byte=serial_port.read()
            serial_string=serial_byte.decode()
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
                self.led1.change_LED_color("yellow")
            if in_string=="F":
                print("F")
                self.led1.change_LED_color("blue")
        

    async def updater(self, interval):
        #This async function manually updates the Tkinter GUI.
        while True:
            self.update()
            await asyncio.sleep(interval)


    def close(self):
        #This function could be cleaned up more.
        tasks=asyncio.all_tasks()
        for task in tasks:
            task.cancel()
        self.destroy()
       

async def main():
    myObj= await DigitalHWLong.taskSetup()
    #Notice here, we don't directly call the constructor of DigitalHWLong because
    #Constructors can't be async. Instead, we call the async function taskSetup which calls
    #the constructor. Also, I do have to define main here. I can't just put this in the
    #if statement below because this main must be an async function.
  
    
     


if __name__=="__main__":
    asyncio.run(main())

     
