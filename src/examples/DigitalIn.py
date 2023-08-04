#This example reads characters in from the microcontroller to the computer
#and prints the result. Be sure to set the correct port for your machine.

import serial
import serial.tools.list_ports as port_list

print('Hello')
#If you are on Windows, uncomment the next line and adjust as needed.
#port='COM1'
#If you are on Linux, uncomment the next line and adjust as needed.
port='/dev/ttyACM0'
baudrate=115200
serialPort=serial.Serial(port=port, baudrate=baudrate, \
            bytesize=8, timeout=0.1, stopbits=serial.STOPBITS_TWO)
while True:
    serialString=serialPort.read()
    print(serialString)
serialPort.close()
