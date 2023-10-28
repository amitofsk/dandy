#When you run this example, you see two buttons and a knob. To turn the knob,
#put your cursor on it and click with either the left or right mouse button.
#When you click the top button, a float representing the knob value
#is both printed and sent serially down the USB cable. The bottom button
#is a quit button. All messages sent via USB end in the character X to
#identify the end of the message.
#
#The dial controls the number of steps the motor takes in going from a
#fixed starting angle to a fixed stopping angle. Therefore, the larger
#the value on the dial, the more steps are taken with a fixed delay between
#steps, and therefore the slower the motor rotates.

import tkinter as tk
import time
import serial
import serial.tools.list_ports as port_list
import sys
sys.path.append('../widgets') 
import KnobDisplay as kd

#If you are on Windows, uncomment the next line and adjust as needed.
PORT='COM1'
#If you are on Linux, uncomment the next line and adjust as needed.
#PORT='/dev/ttyACM0'

class MotorControl(tk.Tk):
    def __init__(self):
        super().__init__()
        self.canvasK=tk.Canvas(self, height=300, width=300)
        self.offset=5
        self.value=0
        baudrate=115200
        self.serial_port=serial.Serial(port=PORT, baudrate=baudrate, \
                    bytesize=8, timeout=0.1, stopbits=serial.STOPBITS_TWO)

        self.button1= tk.Button(self, text="Send Value", command=self.toggle_me)
        self.knob1=kd.KnobDisplay(self.canvasK, width=100, height=100)
        self.button_quit=tk.Button(self, text="Quit", command=self.destroy)
        
        self.button1.pack()
        self.canvasK.pack()
        self.knob1.pack()
        self.button_quit.pack()

        #We don't run Tkinter's main loop. Instead, we run the function
        #updater, which we define below. That function manually updates
        #the Tkinter loop.
        self.updater()
        

    def toggle_me(self):
        message=str(self.value)
        message=message+'X'
        byteMessage=bytes(message, 'utf-8')
        print(byteMessage)
        self.serial_port.write(byteMessage)
        self.update()


    def updater(self):
        #This function manually updates the GUI repeatedly in a loop.
        while True:
            time.sleep(.1)
            self.value=self.offset+self.knob1.get_angle()
            self.update()

if __name__=="__main__":
    mygui=MotorControl()
    
