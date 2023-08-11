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

