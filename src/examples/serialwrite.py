import serial
import serial.tools.list_ports as port_list
import time

print('Hello')
#ports=list(port_list.comports())
#port=(ports[0].device)
#print(ports[0].device)
#If you are on Windows and get an error saying port not found, try the next line.
#port='COM1'
#If you are on Linux and get an error saying port not found, try the next line.
port='/dev/ttyACM0'
baudrate=115200
serialPort=serial.Serial(port=port, baudrate=baudrate, bytesize=8, timeout=0.1, stopbits=serial.STOPBITS_TWO)
while True:
    #serialString=serialPort.read()
    #print(serialString)
    serialPort.write(bytes('Z', 'utf-8'))
    print('I said Z')
    time.sleep(1)
serialPort.close()
