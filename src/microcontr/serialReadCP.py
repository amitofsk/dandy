#TEST ME... THIS CODE NEEDS DEBUGGING

#Run this code on a Raspberry Pi Pico with CircuitPython.
#This program reads a character from the computer into the microcontroller.
#When a character is received, the LED blinks.

import time
import board
import digitalio
import supervisor

print ("hello")
led=DigitalInOut(board.LED)
led.direction=digitalio.Direction.OUTPUT

while True:
    if supervisor.runtime.serial_bytes_available:
        #read in a character
        ch=input().strip()
        print(ch)
        led.value(True)
        time.sleep(0.25)
        led.value(False)
    time.sleep(1)
