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
#The following sites were used as a reference for low level pwm control:
#https://microcontrollerslab.com/servo-motor-raspberry-pi-pico-micropython/ 
#https://github.com/Infineon/micropython/blob/ports-psoc6-ifx/docs/psoc6/quickref.rst

#Oddly, this worked when connecting the motor's yellow wire to pin 6.1
#but not 6.0 for me.

from time import sleep
from machine import Pin, PWM
pwm = PWM('P6_1', freq=50, duty_u16=2000, invert=0)

for i in range(5):
    steps=20*i+20   #Set number of steps.
    #Rotate forward
    for position in range(1000,9000,steps):
        pwm.duty_u16(position)
        sleep(0.01)
    #rotate back
    for position in range(9000,1000,-1*steps):
        pwm.duty_u16(position)
        sleep(0.01)
        
pwm.deinit()
