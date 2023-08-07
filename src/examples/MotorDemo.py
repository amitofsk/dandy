#When you run this example, the computer sends the character 'Z' to
#the microcontroller every second. Make sure to set port correctly.

import serial
import serial.tools.list_ports as port_list
import time

print('Hello')
#Set your serial port.
#On Windows, uncomment the line below and replace COM1 with the appropriate port.
#port='COM1'
#On Linux, uncomment the line below.
port='/dev/ttyACM0'
baudrate=115200
serialPort=serial.Serial(port=port, baudrate=baudrate, bytesize=8, \
                         timeout=0.1, stopbits=serial.STOPBITS_TWO)
while True:
    #serialString=serialPort.read()
    #print(serialString)
    #json1="{\"timeLength\":\"1\",\"speed\":\"5\"}"
    msg="8"
    serialPort.write(bytes(msg, 'utf-8'))
    print('I wrote 8')
    time.sleep(1)
serialPort.close()
