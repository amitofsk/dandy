#This example rotates the motor. Each of the five times through the for loop,
#the motor spins at a different speed. In each of theses times through the loop,
#the motor spins to a fixed location forward then back.
#
#The rotation speed is actually controlled by the number of steps in the
#motor rotation because there is a 10ms delay between each steps.
#While the command pwm.freq() sets the pwm frequency, this command was not
#used for controlling the speed because it was just too fast to be observable.
#The number of steps was used instead because it allowed for slower speeds which
#are observable.
#
#References:
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

