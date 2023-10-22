#Reference on asyncio and MicroPython and the RPi:
#https://www.digikey.com/en/maker/projects/getting-started-with-asyncio-in-micropython-raspberry-pi-pico/110b4243a2f544b6af60411a85f0437c

#MicroPython and deques:
#https://docs.micropython.org/en/latest/library/collections.html
#https://github.com/micropython/micropython-lib/blob/master/python-stdlib/collections-deque/collections/deque.py

#CircuitPython also has a deque in the collections class.
#https://docs.circuitpython.org/en/latest/docs/library/collections.html

#More refs:
#https://learn.adafruit.com/cooperative-multitasking-in-circuitpython-with-asyncio/overview
#https://learn.adafruit.com/keep-your-circuitpython-libraries-on-devices-up-to-date-with-circup

import board
import pwmio
import time
import digitalio
import sys
import asyncio
import collections
import select

# Settings and globals
led=digitalio.DigitalInOut(board.LED)
led.direction=digitalio.Direction.OUTPUT
pwm = pwmio.PWMOut(board.GP1, frequency=50)
led.value=False
steps=50
# setup poll to read USB port
poll_object = select.poll()
poll_object.register(sys.stdin,1)

#Set up a global deque that can store up to 100 elements
q=()
bigq=collections.deque(q, 100)

# The use_serial_data task reads from the deque and uses what it finds to change the motor spin speed.
#Pick stuff off from the deque until you get 'X'. Then, reassemble the number you found.
#Then, spin the motor at that speed.
#The advantage of splitting up the check_serial_data and use_serial_data tasks is that
#the microcontroller can continue to read, even if the motor is still spinning.
async def use_serial_data():
    print('Started use_serial_data task')
    val='Z'
    steps=50
    tempMessage=''
    tempNum=0.0
    while True:
        #Check if the deque is not empty
        if bigq:
            #Pop stuff off the deque.
            val= bigq.popleft()
            #If val is not X, it is part of a number.
            if val != 'X':
                #Concatenate the values you read into a string.
                tempMessage=tempMessage+val
                led.value=True
            #If val is X, you've reached the end of the number.
            else:
                #The first character is garbage. Drop it.
                tempMessage=tempMessage[-1:]
                #print(tempMessage)
                #Cast the bytes you received to a float.
                tempNum=float(tempMessage)
                #print(tempNum)
                led.value=False
                #We read in floating point values 0.0 to 10.0.
                #We multiply by 10 and cast to integer so the motor steps vary 0 to 100.
                steps=int(tempNum*10)
                print(steps)
                #Reset some variables so we are ready to for the next number.
                tempMessage=''
                tempNum=0
                val='Z'
                await spin_motor(steps)
        await asyncio.sleep(.2)


# The check_serial_data task reads serially from USB and puts what it finds in the deque.
#Read a character at a time and shove it in the deque.
#Assume the transmitter ends each message with 'X'.
async def check_serial_data():
    print('Started check_serial_data task')
    ch='X'
    while True:
        await asyncio.sleep(.2)
        #read as character and put in queue
        if poll_object.poll(0):
            ch =  sys.stdin.read(1)
            print (ch)
            bigq.append(ch)


# The spin_motor task spins the motor at the desired speed.
#Note, it is really the number of steps and delays between each step that set the speed,
#not the actual pwm frequency. This task spins the motor forward and back.
async def spin_motor(mySteps):
    print('Started spin_motor task')
    #Rotate forward
    print(mySteps)
    for j in range(mySteps):
        duty_cyc=1.0*j/(steps);
        pwm.duty_cycle=int(65535.0*duty_cyc/10.0)
        time.sleep(0.150)

    #rotate back
    for j in range(steps):
        duty_cyc=(1-(1.0*j/(steps)))
        pwm.duty_cycle=int(65535.0*duty_cyc/10.0)
        time.sleep(0.150)
    await asyncio.sleep(0.1)
    #print('z')


##Define the main function.
async def main():
    print("Hello")
    # Start the three tasks and immediately return
    asyncio.create_task(use_serial_data())
    asyncio.create_task(check_serial_data())
    asyncio.create_task(spin_motor(steps))

    await check_serial_data()


#Run the main loop
asyncio.run(main())

