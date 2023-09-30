#When you run this example, the computer sends the character 'Z' to
#the microcontroller every second. Make sure to set PORT for your machine.

import serial
import serial.tools.list_ports as port_list
import time

#Set up PORT.
#If you are on Windows, uncomment the next line and adjust as needed.
#PORT='COM1'
#If you are on Linux, uncomment the next line and adjust as needed.
PORT='/dev/ttyACM0'

class DigitalOut():
    baudrate=115200
    serialPort=serial.Serial(port=PORT, baudrate=baudrate, bytesize=8, \
                         timeout=0.1, stopbits=serial.STOPBITS_TWO)
    while True:
        serialPort.write(bytes('80', 'utf-8'))
        print('I wrote Z')
        time.sleep(3) 
    serialPort.close()

if __name__=="__main__":
    example=DigitalOut()
