#TEST ME... THIS CODE NEEDS DEBUGGING

#Run this code on a Raspberry Pi Pico with CircuitPython.
#Wire a pushbutton to pin 21 (GP16).
#This program sends characters from the microcontroller to a computer
#and controls an LED.

import time
import board
import digitalio

print ("hello")
led=DigitalInOut(board.LED)
led.direction=digitalio.Direction.OUTPUT
button=DigitalInOut(board.GP16)
button.direction=digitalio.Direction.INPUT
button.PULL.DOWN
while True:
    if button.value():
        print("T")
        led.value(True)
    else:
        print("F")
        led.value(False)
    time.sleep(1)

