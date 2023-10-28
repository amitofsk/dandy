#This example reads an analog value from pin 10.0, puts together a message
#in JSON format, and prints it. This example assumes you are using a
#PSoC microcontroller coded in MicroPython.

from machine import Pin
from machine import ADC
import time
print ("hello")

adc=ADC(Pin("P10_0"))

value=0
while True:
    value=adc.read_u16()
    outstring='{\"boardNumber\":\"1\", \"boardType\":\"RPi\", \"value\":\"'+str(value)+'\"}'
    print(outstring)
    time.sleep(1)
