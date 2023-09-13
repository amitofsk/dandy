
#This exaple closely follows reference
#https://microcontrollerslab.com/servo-motor-raspberry-pi-pico-micropython/
#It demonstrates rotating the motor at four different speeds
from time import sleep
from machine import Pin, PWM

pwm = PWM(Pin(1))

for i in range(5):
    #Set to a new speed
    speed=20*i+20
    pwm.freq(speed)
    #Rotate forward
    for position in range(1000,9000,50):
        pwm.duty_u16(position)
        sleep(0.01)
    #rotate back
    for position in range(9000,1000,-50):
        pwm.duty_u16(position)
        sleep(0.01)

