#Reference on communicating with the sensor:
#https://community.infineon.com/t5/Knowledge-Base-Articles/XENSIV-TLI493D-W2BW-I2C-interface-example-KBA237409/ta-p/437707

#Reference on sensor data format:
#https://www.infineon.com/dgdl/Infineon-TLI_493D-W2BW-UserManual-v01_10-EN.pdf?fileId=5546d46273a5366f0173be229e1b1512
#Reference on MicroPython and the RPi
#https://docs.micropython.org/en/latest/rp2/quickref.html

#This example reads info from the TLE493D-W2B6 3D Magnetic field sensor
#and prints the result in json format. Before starting, connect 3.3V (pin 36),
#Gnd (pin 38), SDA to RPi pin21 (GP16), and SCL to RPi pin 22 (GP17). (or is it 6,7?)

#Ref on micropython and i2c
##https://www.digikey.com/en/maker/projects/raspberry-pi-pico-rp2040-i2c-example-with-micropython-and-cc/47d0c922b79342779cdbd4b37b7eb7e2
#https://github.com/Infineon/micropython/blob/ports-psoc6-ifx/docs/psoc6/quickref.rst


from machine import I2C, Pin, SoftI2C
import time

i2c=I2C(0,sda=Pin(16), scl=Pin(17))
ADDRESS=0x35

devices=i2c.scan()
if devices:
    for d in devices:
        print(hex(d))
else:
    print('here')

#Bus setup
#writebuf=hex(0x10)
#i2c.writeto(ADDRESS, bin(16))
#writebuf=hex(0b00010001)
#i2c.writeto(ADDRESS, bin(17))
#writebuf=hex(0b10010001)
#i2c.writeto(ADDRESS, bin(145))
msg=bytearray()
msg.append(0x11)
msg2=bytearray()
msg.append(0x91)
i2c.writeto_mem(ADDRESS, 0x10, msg)
i2c.writeto_mem(ADDRESS, 0x10, msg2)


#Eventually read from the sensor

#print(writebuf)
#Print result in json format...
while True:
    print('hello')
    #OK.. I'm reading the data here... I have to pick it off still
    #and put it in int form.

    #Read 7 registers from the i2c bus
    data=i2c.readfrom(ADDRESS, 7)

    #Pick off the individual hex bytes and reassemble them.
    #Does int round or truncate? I want truncate here.
    X_first_hex=int(data[0]/16)
    X_second_hex=data[0]%16
    X_third_hex=int(data[4]/16)
    BX=X_first_hex*256+X_second_hex*16+X_third_hex
    Y_first_hex=int(data[1]/16)
    Y_second_hex=data[1]%16
    Y_third_hex=data[4]%16
    BY=Y_first_hex*256+Y_second_hex*16+Y_third_hex
    Z_first_hex=int(data[2]/16)
    Z_second_hex=data[2]%16
    Z_third_hex=data[5]%16
    BZ=Z_first_hex*256+Z_second_hex*16+Z_third_hex
    print(BX, BY, BZ)

    #OK.. number were converted from hexadecimal here, so there
    #is an offset... this is actually good. Do the same in
    #Arduino... In the python computer code, convert by taking
    #away the offset.
    #In other words, numbers 0 to 2048 are positive. If you
    #get a value 2049 to 4096, it really is negative.
    #subtract that value from 4096 and put a minus out front.
    #So 4095 is actually -1.

    #Put data in json format

    print("{\"BX\":\"", BX, "\",\"BY\":\"",BY, "\",\"BZ\":\"", BZ, "\"}")


    time.sleep(1)
