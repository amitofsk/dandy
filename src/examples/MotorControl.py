#When you run this example, you see three speed buttons, a dial, a knob widget,
# a TricolorDisplay LED widget, and a quit button.  When you press a speed
#button, a corresponding speed is printed to the serial USB connection.
#If you dial the knob below a threshhold or above a second threshhold, the
# color of the TricolorDisplay widget changes, and the corresponding speed
#is printed to the serial USB connection too.



import tkinter as tk
import time
import serial
import serial.tools.list_ports as port_list
import sys
sys.path.append('../widgets') 
import KnobDisplay as kd
import TricolorDisplay as td

#If you are on Windows, uncomment the next line and adjust as needed.
#PORT='COM1'
#If you are on Linux, uncomment the next line and adjust as needed.
PORT='/dev/ttyACM0'

class DigitalOutDisplay(tk.Tk):
    def __init__(self):
        super().__init__()
        self.canvasK=tk.Canvas(self, height=300, width=300)
        self.button1= tk.Button(self, text="Speed 10", \
                               command= self.toggle_me(speed=10))
        self.button2=tk.Button(self, text="Speed 20", \
                               command=self.toggle_me(speed=20))
        self.button3=tk.Button(self, text="Speed 30", \
                               command=self.toggle_me(speed=30))
        self.knob1=kd.KnobDisplay(self.canvasK, width=100, height=100)
        self.led1=td.TricolorDisplay(self)
        self.button_quit=tk.Button(self, text="Quit", command=self.destroy)
        self.offset=5
        self.value=0
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        self.canvasK.pack()
        self.knob1.pack()
        self.led1.pack()
        self.button_quit.pack()

       
        baudrate=115200
       # self.serial_port=serial.Serial(port=PORT, baudrate=baudrate, \
       #                 bytesize=8, timeout=0.1, stopbits=serial.STOPBITS_TWO)
        
        #We don't run Tkinter's main loop. Instead, we run the function
        #updater, which we define below. That function manually updates
        #the Tkinter loop.
        self.updater()


    def toggle_me(self, speed):
        out_string='A'
        print('I wrote A '+str(speed))
        #TODO: Change from writing a character to a string
        #The function bytes casts a string to bytes.
        #self.serial_port.write(bytes(out_string,'utf-8'))
        self.update()


    def updater(self):
        while True:
            time.sleep(.1)
            print(self.value)
            self.value=self.offset+self.knob1.get_angle()
            #Insert here...serial write and change Tricolor and comparator...
            #Manually check buttons?
            self.update()

if __name__=="__main__":
    mygui=DigitalOutDisplay()
    
