//This example closely follows the example at  
//https://community.infineon.com/t5/Knowledge-Base-Articles/XENSIV-TLI493D-W2BW-I2C-interface-example-KBA237409/ta-p/437707
//Sensor data format is from:
//https://www.infineon.com/dgdl/Infineon-TLI_493D-W2BW-UserManual-v01_10-EN.pdf?fileId=5546d46273a5366f0173be229e1b1512
//This example reads info from the TLE493D-W2B6 3D Magnetic field sensor and prints the result in json format.
//Before starting, connect 3.3V, Gnd, SDA, and SDL of the sensor to the Arduino.

#include <Wire.h>
#define ADDRESS 0x35 //Addreass of the sensor on the I2C bus

int16_t BX=0;
int16_t BY=0;
int16_t BZ=0;
int16_t T=0;
void setup() {
 
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
   //Setup Serial for talking to the computer
   Serial.begin(115200);
   //Set up variables we'll need

 }


void loop () {
  
  //Read in the first seven registers from the sensor which contain the magnetic values.
  uint8_t buf[7];
  Wire.requestFrom(ADDRESS, 7);
  for (uint8_t i = 0; i < 7; i++) {
    buf[i] = Wire.read();
  }

  //The 8 MSB of BX are stored in register 0, and the 4 LSB of BX are in register 4.
  //The 8 MSB of BY are stored in register 1, and the 4 LSB of BY are in register 4
  //The 8 MSB of BZ are stored in register 2, and the 4 LSB of BZ are in regiester 5.
  //We pick off these values and store them in X, Y, and Z
  //These lines come straight from the exaple cited at the top. 
  BX = (int16_t)((buf[0] << 8 )| (buf[4] & 0xF0)) >> 4;
  BY = (int16_t)((buf[1] << 8 ) | ((buf[4] & 0x0F) << 4)) >> 4;
  BZ = (int16_t)((buf[2] << 8 ) | ((buf[5] & 0x0F) << 4)) >> 4;
  T = (buf[3] << 4) | (buf[5] >> 4);


  //TODO: Add offset instead of zeroing out here? Send in a different data type?
  if (BX<0) {BX=0;}
  if (BY<0) {BY=0;}
  if(BZ<0) {BZ=0;}

  //Serially print the result in json format.
  Serial.print("\{\"BX\":\"");
  Serial.print(BX);
  Serial.print("\",\"BY\":\"");
  Serial.print(BY);
  Serial.print("\",\"BZ\":\"");
  Serial.print(BZ);
  Serial.println("\"\}");
  delay(500);
  
  
}

