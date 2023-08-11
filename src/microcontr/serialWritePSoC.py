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
