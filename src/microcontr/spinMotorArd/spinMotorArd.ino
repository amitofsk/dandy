//References:
// LED:   https://www.arduino.cc/en/Tutorial/BuiltInExamples/Blink
// Servo: https://www.instructables.com/Arduino-Servo-Motors/


// Include the Time library
#include <time.h>

// Include the Servo library
#include <Servo.h>

// Declare the Servo pin
int servoPin = 9;

// Create a servo object
Servo Servo1;
void setup() {

   // We need to attach the servo to the used pin number
   Servo1.attach(servoPin);

  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);

}

void loop(){
   // Make servo go to 0 degrees
   Servo1.write(0);
   digitalWrite(LED_BUILTIN, LOW);   // turn the LED off by making the voltage LOW
   delay(7000);                      // wait for 7 seconds
   // Make servo go to 90 degrees
   Servo1.write(80);
   digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)
   delay(7000);                      // wait for 7 seconds

   // Make servo go to 180 degrees
   //Servo1.write(180);
   //delay(10000);


   Serial.println(millis());
   Serial.print(__TIME__);

}
