##TODO: CUT THIS EXAMPLE... IT WAS ONLY USED FOR TESTING

#The purpose of this code is to read from the serial port.
#Reference https://gist.github.com/yptheangel/fcd62ad59a569ace75eb07025b8e9c4f

import serial
import serial.tools.list_ports as port_list
import json

print('Hello World')
#For Windows, uncomment the next line and adjust as needed.
#port='COM1'
#For Linux, uncomment the next line and adjust as needed.
port='/dev/ttyACM0'
baudrate=115200
serialPort=serial.Serial(port=port, baudrate=baudrate, \
            bytesize=8, timeout=0.1, stopbits=serial.STOPBITS_TWO)

while True:
    #Read until you see the two end characters '\r\n'
    serial_string=serialPort.read_until('\r\n')
    #Convert the bytes read into an actual string.
    serial_string=serial_string.decode('utf-8')
    if serial_string!="":
        #Slice off the two end characters
        serial_string=serial_string[:-2]
        #Parse the json and save the result in serial_json
        serial_json=json.loads(serial_string)
        #Pick off the element named "value" of the json
        val=serial_json["value"]
        print(serial_string)
        print(val)

serialPort.close()

