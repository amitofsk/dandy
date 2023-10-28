#Reference on asyncio and MicroPython and the RPi:
#https://www.digikey.com/en/maker/projects/getting-started-with-asyncio-in-micropython-raspberry-pi-pico/110b4243a2f544b6af60411a85f0437c

#A reference on the Queue class that I used for a while but not in the final version:
#https://github.com/peterhinch/micropython-async/blob/master/v3/primitives/queue.py
#References on heapq and the queue instructions I also ended up not using:
#https://docs.micropython.org/en/latest/library/heapq.html
#https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/

#References on the deque I ended up using:
#https://docs.micropython.org/en/latest/library/collections.html
#https://github.com/micropython/micropython-lib/blob/master/python-stdlib/collections-deque/collections/deque.py

#This example does not currently work. It needs more debugging.
#It compiles, but doesn't do what it is supposed to do.
#MicroPython for the PSoC doesn't have the poll instruction,
#so I think that is the main problem here. 

from time import sleep
from machine import Pin, PWM
import sys
import uasyncio as asyncio
import collections
import select

# Settings and globals
pwm = PWM('P6_0', freq=50, duty_u16=2000, invert=0)
#pwm = PWM(Pin(1))
led=Pin(25, Pin.OUT)
led.value(False)
steps=50
# setup poll to read USB port
#poll_object = select.poll()
#poll_object.register(sys.stdin,1)

#Set up a global deque that can store up to 100 elements
q=()
bigq=collections.deque(q, 100)

# The use_serial_data task reads from the deque and uses what it finds to change the motor spin speed.
#Pick stuff off from the deque until you get 'X'. Then, reassemble the number you found.
#Then, spin the motor at that speed.
#The advantage of splitting up the check_serial_data and use_serial_data tasks is that...
#You can read ahead, even if the motor is still spinning...
async def use_serial_data():
    print('Started use_serial_data task')
    val='Z'
    steps=50
    tempMessage=''
    tempNum=0.0
    while True:
        if bigq: #Check if the deque is not empty
            #Pop stuff off the deque. If it is not X, it is part of a number.
            #Concatenate to a string.
            #If it is X, you've reached the end of the number. Convert string to float and spin motor.
            val= bigq.popleft()
            if val != 'X':
                tempMessage=tempMessage+val
                led.value(True)
            else:
                tempMessage=tempMessage[-1:] #The first character is garbage. Drop it.
                print(tempMessage)
                tempNum=float(tempMessage)
                print(tempNum)
                led.value(False)
                steps=int(tempNum*10)
                print(steps)
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
        #if poll_object.poll(0):
            ch =  sys.stdin.read(1)
            print (ch)
            bigq.append(ch)


# The spin_motor task spins the motor at the desired speed.
#Note, it is really the number of steps and delays between each step that set the speed,
#not the actual pwm frequency.
#This spins the motor forward and back.
async def spin_motor(mySteps):
    print('Started spin_motor task')
    #Rotate forward
    print(mySteps)
    for position in range(1000,9000,mySteps):
        pwm.duty_u16(position)
        await asyncio.sleep(0.1)
    #rotate back
    for position in range(9000,1000,-1*mySteps):
        pwm.duty_u16(position)
        await asyncio.sleep(0.1)
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
