#Run this code on a PSoC with MicroPython.
#This program reads a character from the computer into the microcontroller.
#When a character is received, the LED blinks.

from machine import Pin
import time
import sys
print ("hello")

led=Pin("P13_7", Pin.OUT)
led.value(False)
while True:
    #read as character
    ch = sys.stdin.read(1)
    print (ch)
    led.value(False)
    time.sleep(0.25)
    led.value(True)
    time.sleep(1)

