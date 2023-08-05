from machine import Pin
from machine import ADC
import time
print ("hello")

adc=ADC(Pin(26 ))

value=0
while True:
    value=adc.read_u16()
    outstring='{\"boardName\":\"RPP1\", \"pinName\":\"ADC0\", \"value\":\"'+str(value)+'\"}'
    print(outstring)
    time.sleep(1)
