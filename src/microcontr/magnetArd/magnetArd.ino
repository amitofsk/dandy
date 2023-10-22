/*
This example reads info from the TLE493D-W2B6 3D magnetic field sensor and prints 
the result in json format. Before starting, connect SDA, SDC, power (3.3V), and GND of the sensor to 
the Arduino. 

This example closely follows the example at: 
https://community.infineon.com/t5/Knowledge-Base-Articles/XENSIV-TLI493D-W2BW-I2C-interface-example-KBA237409/ta-p/437707

Reference on communicating with the sensor:
https://community.infineon.com/t5/Knowledge-Base-Articles/XENSIV-TLI493D-W2BW-I2C-interface-example-KBA237409/ta-p/437707

Reference on sensor data format:
https://www.infineon.com/dgdl/Infineon-TLI_493D-W2BW-UserManual-v01_10-EN.pdf?fileId=5546d46273a5366f0173be229e1b1512
*/


#include <Wire.h>
#define ADDRESS 0x35 //Addreass of the sensor on the I2C bus

int16_t BX=0;
int16_t BY=0;
int16_t BZ=0;
int16_t T=0;
void setup() {
   Serial.begin(115200);
   //Setup I2C for talking to the sensor
   Wire.begin();
   Wire.beginTransmission(ADDRESS);
   //Here we set up the configuration register 10.
   //We set bit DT to 0 indicating we want to measure temperature.
   //We set bit AM to 0 indicating we want to measure BZ.
   //We set bits TRIG to 01 to triger on read before first most significant bit.
   //We set bits X2 and TL_mag to 000 for more sensitivity and no temperature correction.
   //We set bit CP to 1 for odd parity.
   Wire.write(0x10);
   Wire.write(0b00010001); 
   Wire.write(0b10010001); 
   Wire.endTransmission();
 }


void loop () {
  int X_first_hex, X_second_hex, X_third_hex, BX;
  int Y_first_hex, Y_second_hex, Y_third_hex, BY;
  int Z_first_hex, Z_second_hex, Z_third_hex, BZ;
  
  //Read in the first seven registers from the sensor which contain the magnetic values.
  uint8_t buf[7];
  Wire.requestFrom(ADDRESS, 7);
  for (uint8_t i = 0; i < 7; i++) {
    buf[i] = Wire.read();
  }

  //Start with the X component of the magnetic field. Pick off each of the three
  //hexadecimal bytes. Reassemble them so the result is an itneger. 
  X_first_hex=int(buf[0]/16);
  X_second_hex=buf[0]%16;
  X_third_hex=int(buf[4]/16);
  BX=X_first_hex*256+X_second_hex*16+X_third_hex;
  //The if statement converts it to a signed value.
  if (BX>2048)
    {BX=-1*(4096-BX);}

  //Do the same for the Y component of the magnetic field.
  Y_first_hex=int(buf[1]/16);
  Y_second_hex=buf[1]%16;
  Y_third_hex=buf[4]%16;
  BY=Y_first_hex*256+Y_second_hex*16+Y_third_hex;
  if (BY>2048)
    {BY=-1*(4096-BY);}
  
  //Do the same for the Z component of the magnetic field. 
  Z_first_hex=int(buf[2]/16);
  Z_second_hex=buf[2]%16;
  Z_third_hex=buf[5]%16;
  BZ=Z_first_hex*256+Z_second_hex*16+Z_third_hex;
  if (BZ>2048)
    {BZ=-1*(4096-BZ);}

  //Assemble a string in JSON format containing BX, BY, and BZ, and print it.
  Serial.print("\{\"BX\":\"");
  Serial.print(BX);
  Serial.print("\",\"BY\":\"");
  Serial.print(BY);
  Serial.print("\",\"BZ\":\"");
  Serial.print(BZ);
  Serial.println("\"\}");
  delay(500);  
}

