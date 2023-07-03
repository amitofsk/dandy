#The purpose of this code is to read from the serial port...
#pip install pyserial
#Reference https://gist.github.com/yptheangel/fcd62ad59a569ace75eb07025b8e9c4f
import serial
import serial.tools.list_ports as port_list

print('Hello World')
ports=list(port_list.comports())
#print(ports[0].device)
port='/dev/ttyACM0'
baudrate=115200
serialPort=serial.Serial(port=port, baudrate=baudrate, bytesize=8, timeout=0.1, stopbits=serial.STOPBITS_TWO)
imax=100

for ii in range(imax):
    serialString=serialPort.read()
    print(serialString)

serialPort.close()

