#When you run this example, you see three speed buttons, a dial, a knob widget,
# a TricolorDisplay LED widget, and a quit button.  When you press a speed
#button, a corresponding speed is printed to the serial USB connection.
#If you dial the knob below a threshhold or above a second threshhold, the
# color of the TricolorDisplay widget changes, and the corresponding speed
#is printed to the serial USB connection too.

#Reference of use of lambda function for the button command:
#https://www.geeksforgeeks.org/how-to-pass-arguments-to-tkinter-button-command/

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

class MotorControl(tk.Tk):
    def __init__(self):
        super().__init__()
        self.canvasK=tk.Canvas(self, height=300, width=300)
        self.offset=5
        self.value=0
        baudrate=115200
        self.serial_port=serial.Serial(port=PORT, baudrate=baudrate, \
                    bytesize=8, timeout=0.1, stopbits=serial.STOPBITS_TWO)
        
        
        self.button1= tk.Button(self, text="Send Value", \
                               #command=lambda: self.toggle_me(speed=self.value))
                            command=self.toggle_me)
        #self.button2=tk.Button(self, text="Send B", \
        #                       command=lambda: self.toggle_me(speed=self.value))
        #self.button3=tk.Button(self, text="Send C", \
        #                       command=lambda: self.toggle_me(speed=30))
        self.knob1=kd.KnobDisplay(self.canvasK, width=100, height=100)
        #self.led1=td.TricolorDisplay(self)
        self.button_quit=tk.Button(self, text="Quit", command=self.destroy)
        
        self.button1.pack()
        #self.button2.pack()
        #self.button3.pack()
        self.canvasK.pack()
        self.knob1.pack()
        #self.led1.pack()
        self.button_quit.pack()

       
        #We don't run Tkinter's main loop. Instead, we run the function
        #updater, which we define below. That function manually updates
        #the Tkinter loop.
        self.updater()
        #tk.mainloop()

    def toggle_me(self):
        #print("HERE")
        #out_string='A'
         
        #print('I wrote A '+str(speed))
        message=str(self.value)
        message=message+'X'
        byteMessage=bytes(message, 'utf-8')
        print(byteMessage)
        self.serial_port.write(byteMessage)
        #if speed==10:
        #    self.serial_port.write(bytes('5.2', 'utf-8'))
        #    print('A')
        #    print(self.value)
        
        #elif speed==30:
        #    self.serial_port.write(bytes('C', 'utf-8'))
        #    print('C')
        #else :
        #    self.serial_port.write(message)
        #    print('B')
        #    print(self.value)
        #TODO: Change from writing a character to a string
        #The function bytes casts a string to bytes.
        #self.serial_port.write(bytes(out_string,'utf-8'))
        self.update()


    def updater(self):
        while True:
            time.sleep(.1)
            #print(self.value)
            self.value=self.offset+self.knob1.get_angle()
            #Insert here...serial write and change Tricolor and comparator...
            #Manually check buttons?
            self.update()

if __name__=="__main__":
    mygui=MotorControl()
    
