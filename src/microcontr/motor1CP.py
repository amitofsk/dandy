#This example closely follows reference
#https://microcontrollerslab.com/servo-motor-raspberry-pi-pico-micropython/
#It demonstrates rotating the motor at four different speeds

#Circuit python ref:
#https://learn.adafruit.com/using-servos-with-circuitpython/low-level-servo-control

import board
import pwmio
import pulseio
import time
import digitalio
# Create a function to simplify setting PWM duty cycle for the servo:
def servo_duty_cycle(pulse_ms, frequency=50):
    period_ms = 1.5*1.0 / frequency * 1000.0
    duty_cycle = int(pulse_ms / (period_ms / 65535.0))
    return duty_cycle


led=digitalio.DigitalInOut(board.LED)
led.direction=digitalio.Direction.OUTPUT
pwm = pwmio.PWMOut(board.GP1, frequency=50)
#speed=50
#print('hey')
#led.value=True


#The value 1000*i represents the number of steps taken.
#The variable j represents the step number.
#We're rotating between pulse_ms=1.0 and pulse_ms=4.0 here.
#The speed is purposely set slow so that it is more observable.
for i in range (5):
    steps = 1000*i
    #Spin forward
    led.value=True
    for j in range(steps):
        pulse_ms_value=1.0+j*.003/(1.0*i)
        pwm.duty_cycle=servo_duty_cycle(pulse_ms_value)
        time.sleep(0.005)

    #Spin reverse 3000 steps
    led.value=False
    for j in range(steps):
        pulse_ms_value=4.0-j*.003/(1.0*i)
        pwm.duty_cycle=servo_duty_cycle(pulse_ms_value)
        time.sleep(0.005)


