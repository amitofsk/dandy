#This example reads an analog value from pin GP26, puts together a message
#in JSON format, and prints it. This example assumes you are using a
#Raspberry Pi Pico microcontroller coded in MicroPython.

from machine import Pin
from machine import ADC
import time
print ("hello")

adc=ADC(Pin(26 ))

value=0
while True:
    value=adc.read_u16()
    outstring='{\"boardNumber\":\"1\", \"boardType\":\"RPi\", \"value\":\"'+str(value)+'\"}'
    print(outstring)
    time.sleep(1)
