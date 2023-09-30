#This example closely follows reference
#https://microcontrollerslab.com/servo-motor-raspberry-pi-pico-micropython/
#It demonstrates rotating the motor at four different speeds

#Circuit python ref:
#https://learn.adafruit.com/using-servos-with-circuitpython/low-level-servo-control
#THIS STILL NEEDS DEBUGGING, but its a start...

import board
import pwmio
import pulseio
import time
import digitalio

servo = pwmio.PWMOut(board.GP1, frequency=50)

# Create a function to simplify setting PWM duty cycle for the servo:
def servo_duty_cycle(pulse_ms, frequency=50):
    period_ms = 1.0 / frequency * 1000.0
    duty_cycle = int(pulse_ms / (period_ms / 65535.0))
    return duty_cycle

for i in range (5):
    speed=20*i+20
    servo.duty_cycle = servo_duty_cycle(1.0, frequency=speed)
    time.sleep(1.0)
    servo.duty_cycle = servo_duty_cycle(2.0, frequency=speed)
    time.sleep(1.0)

