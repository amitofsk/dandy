#Run this code on a Raspberry Pi Pico with CircuitPython.
#This program reads a character from the computer into the microcontroller.

#References used:
#https://github.com/Neradoc/circuitpython-sample-scripts/blob/main/usb_serial/README.md
#https://docs.circuitpython.org/en/latest/shared-bindings/usb_cdc/index.html

import time
import board
import digitalio
import supervisor
import usb_cdc

print ("hello")
led=digitalio.DigitalInOut(board.LED)
led.direction=digitalio.Direction.OUTPUT
serial=usb_cdc.data

while True:
    if serial.in_waiting >0:
        ch=serial.read()
        print(ch)
        led.value=True
        time.sleep(0.25)
        led.value=False
        time.sleep(1)

