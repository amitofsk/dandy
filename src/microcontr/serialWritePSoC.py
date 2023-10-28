#This program sends characters from the microcontroller to a computer
#and controls an LED. It assumes you are writing code for a 
#PSoC microcontroller in MicroPython. Wire a pushbutton to pin 0.4.

from machine import Pin
import time
print ("hello")

button = Pin("P0_4", Pin.IN, Pin.PULL_DOWN)
led=Pin("P13_7", Pin.OUT)
while True:
    if button.value():
        print("F")
        led.value(True)
    else:
        print("T")
        led.value(False)
    time.sleep(1)
