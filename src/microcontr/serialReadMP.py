#Run this code on a Raspberry Pi Pico with MicroPython.
#This program reads a character from the computer into the microcontroller.
#When a character is received, the LED blinks.

from machine import Pin
import time
import select
import sys
print ("hello")

led=Pin(25, Pin.OUT)
led.value(True)
# setup poll to read USB port
poll_object = select.poll()
poll_object.register(sys.stdin,1)
while True:
    if poll_object.poll(0):
        #read as character
        ch = sys.stdin.read(1)
        print (ch)
        led.value(True)
        time.sleep(0.25)
        led.value(False)
    time.sleep(1)
