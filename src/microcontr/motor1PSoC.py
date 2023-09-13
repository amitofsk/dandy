#This exaple closely follows reference
#https://microcontrollerslab.com/servo-motor-raspberry-pi-pico-micropython/
#The following reference was also used: 
#https://github.com/Infineon/micropython/blob/ports-psoc6-ifx/docs/psoc6/quickref.rst

#It demonstrates rotating the motor at four different speeds

from time import sleep
from machine import Pin, PWM
pwm.deinit()
pwm = PWM('P6_0', freq=20, duty_u16=1000, invert=0)

for i in range(5):
    #Set to a new speed
    speed=20*i+100
    pwm.freq(speed)
    print(pwm.freq())
    #Rotate forward
    for position in range(1000,9000,50):
        pwm.duty_u16(position)
        sleep(0.01)
    #rotate back
    for position in range(9000,1000,-50):
        pwm.duty_u16(position)
        sleep(0.01)
pwm.deinit()
