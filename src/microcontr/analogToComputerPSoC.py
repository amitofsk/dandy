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
