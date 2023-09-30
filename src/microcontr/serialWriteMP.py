#Run this code on a Raspberry Pi Pico with MicroPython.
#Wire a pushbutton to pin 21 (GP16).
#This program sends characters from the microcontroller to a computer
#and controls an LED.


from machine import Pin
import time
print ("hello")

button = Pin(16, Pin.IN, Pin.PULL_DOWN)
led=Pin(25, Pin.OUT)
while True:
    if button.value():
        print("T")
        led.value(True)
    else:
        print("F")
        led.value(False)
    time.sleep(1)
