#References
#https://learn.adafruit.com/using-servos-with-circuitpython/low-level-servo-control
#https://microcontrollerslab.com/servo-motor-raspberry-pi-pico-micropython/
 
import board
import pwmio
import time
import digitalio

led=digitalio.DigitalInOut(board.LED)
led.direction=digitalio.Direction.OUTPUT
pwm = pwmio.PWMOut(board.GP1, frequency=50)
steps=50

for i in range (5):
    print('hey')
    steps = 20*i+10
    #Spin forward
    led.value=True
    for j in range(steps):
        duty_cyc=1.0*j/(steps);
        pwm.duty_cycle=int(65535.0*duty_cyc/10.0)
        time.sleep(0.150)
    #Spin reverse 
    led.value=False
    for j in range(steps):
        duty_cyc=(1-(1.0*j/(steps)))
        pwm.duty_cycle=int(65535.0*duty_cyc/10.0)
        time.sleep(0.150)

