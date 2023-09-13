#This example reads info from the TLE493D-W2B6 3D Magnetic field sensor
#and prints the result in json format. Before starting, connect SDA of the sensor to pin 16 of the RPi,
#and connect SCL of the sensor to pin 17 of the RPi. Also connect power of the sensor to pin 36 of the RPi and
#ground of the sensor to pin 38 of the RPi.

#Reference on communicating with the sensor:
#https://community.infineon.com/t5/Knowledge-Base-Articles/XENSIV-TLI493D-W2BW-I2C-interface-example-KBA237409/ta-p/437707

#Reference on sensor data format:
#https://www.infineon.com/dgdl/Infineon-TLI_493D-W2BW-UserManual-v01_10-EN.pdf?fileId=5546d46273a5366f0173be229e1b1512
#Reference on MicroPython and the RPi
#https://docs.micropython.org/en/latest/rp2/quickref.html

#Reference on micropython and i2c
##https://www.digikey.com/en/maker/projects/raspberry-pi-pico-rp2040-i2c-example-with-micropython-and-cc/47d0c922b79342779cdbd4b37b7eb7e2
#https://github.com/Infineon/micropython/blob/ports-psoc6-ifx/docs/psoc6/quickref.rst




from machine import I2C, Pin, SoftI2C
import time
i2c=I2C(0, sda=Pin(16), scl=Pin(17))
ADDRESS=0x35

#Scan to find I2C devices.
devices=i2c.scan()
if devices:
    for d in devices:
        print(hex(d))
else:
    print("No I2C devices found")

#We set up the configuration register 0x10 for communication.
#More specifically, We set bit DT to 0 indicating we want to measure temperature.
#We set bit AM to 0 indicating we want to measure BZ.
#We set bits TRIG to 01 to triger on read before first most significant bit.
#We set bits X2 and TL_mag to 000 for more sensitivity and no temperature correction.
#We set bit CP to 1 for odd parity.
#To do all this, we write the bytes 0x11 and 0x91.
msg=bytearray()
msg.append(0x11)
msg2=bytearray()
msg.append(0x91)
i2c.writeto_mem(ADDRESS, 0x10, msg)
i2c.writeto_mem(ADDRESS, 0x10, msg2)


while True:
    #Read 7 registers from the i2c bus
    data=i2c.readfrom(ADDRESS, 7)

    #Start with the X component of the magnetic field.
    #Pick off each of the three hexadecimal bytes. Reassemble them so the result is an integer.
    X_first_hex=int(data[0]/16)
    X_second_hex=data[0]%16
    X_third_hex=int(data[4]/16)
    BX=X_first_hex*256+X_second_hex*16+X_third_hex
    #Values are in 2's complement. If we get a value between 2058 and 4096, the number is actually negative.
    #The if statement converts it to a signed value.
    if BX>2048:
        BX=-1*(4096-BX)

    #Do the same for the Y component of the magnetic field.
    Y_first_hex=int(data[1]/16)
    Y_second_hex=data[1]%16
    Y_third_hex=data[4]%16
    BY=Y_first_hex*256+Y_second_hex*16+Y_third_hex
    if BY>2048:
        BY=-1*(4096-BY)

    #Do the same for the Z component of the magnetic field.
    Z_first_hex=int(data[2]/16)
    Z_second_hex=data[2]%16
    Z_third_hex=data[5]%16
    BZ=Z_first_hex*256+Z_second_hex*16+Z_third_hex
    if BZ>2048:
        BZ=-1*(4096-BZ)

    #Assemble a string in JSON format containing BX, BY, and BZ, and print it.
    msgString="{\"BX\":\""
    msgString=msgString+str(BX)
    msgString=msgString+"\",\"BY\":\""
    msgString=msgString+str(BY)
    msgString=msgString+"\",\"BZ\":\""
    msgString=msgString+str(BZ)
    msgString=msgString+"\"}"
    print(msgString)

    time.sleep(1)



