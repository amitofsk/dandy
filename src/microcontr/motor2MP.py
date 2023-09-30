#Reference on asyncio and MicroPython and the RPi:
#https://www.digikey.com/en/maker/projects/getting-started-with-asyncio-in-micropython-raspberry-pi-pico/110b4243a2f544b6af60411a85f0437c

#The Queue class comes from:
#https://github.com/peterhinch/micropython-async/blob/master/v3/primitives/queue.py
#For now, I'm just copying this... eventually, I'll try to cite it properly and separate it out...


from time import sleep
from machine import Pin, PWM
import sys


# Settings
pwm = PWM(Pin(1))
led=Pin(25, Pin.OUT)
led.value(False)
pwm.freq(40)

##Coroutine for reading serial and putting it in the queue
async def use_serial_data(q):
    print('started use_serial_data')
    val='Z'
    speed =40
    while True:
        if not q.empty():
           val = await q.get()
           #print('Value=')
           #print(val)
           #led.value(True)
           if (val=='A'):
               speed=30
               led.value(True)
           if(val=='B'):
                speed=70
                led.value(False)
           pwm.freq(speed)

        await asyncio.sleep(.2)
        led.value(False)


##Coroutine for reading from the queue and doing something with it
async def check_serial_data(q):
    print('started check_serial_data')
    ch='X'
    while True:
        #read as character and put in queue
        ch = sys.stdin.read(1)
        print (ch)
        await q.put(ch)
        await asyncio.sleep(.5)
        await asyncio.sleep(0.04)

async def spin_motor():
    print('spinning motor')
    while True:
         #Rotate forward
        for position in range(1000,9000,50):
            pwm.duty_u16(position)

            await asyncio.sleep(0.0001)
        print('Y')
        #rotate back
        for position in range(9000,1000,-50):
            pwm.duty_u16(position)
            await asyncio.sleep(0.0001)
        print('W')
        #await asyncio.sleep(0.0001)


##Main function
async def main():
    print('hey')
    # Queue for passing messages
    q = Queue()

    # Start coroutine as a task and immediately return
    asyncio.create_task(use_serial_data(q))
    asyncio.create_task(check_serial_data(q))
    asyncio.create_task(spin_motor())
    while True:
      #  print('X')
        await spin_motor()
        await check_serial_data(q)
        await use_serial_data(q)



# Start event loop and run entry point coroutine
asyncio.run(main())
