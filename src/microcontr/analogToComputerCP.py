import time
import board
import analogio

print ("hello")

adc=analogio.AnalogIn(board.GP26)

value=0
while True:
    value=adc.value
    outstring='{\"boardNumber\":\"1\", \"boardType\":\"RPi\", \"value\":\"'+str(value)+'\"}'
    print(outstring)
    time.sleep(1)
