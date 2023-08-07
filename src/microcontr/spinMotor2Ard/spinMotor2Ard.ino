//References:
// LED:   https://www.arduino.cc/en/Tutorial/BuiltInExamples/Blink
// Servo: https://www.instructables.com/Arduino-Servo-Motors/
// Json:https://arduinojson.org/v6/example/parser/


// Include the Time library
#include <time.h>
//#include <ArduinoJson.h>
// Include the Servo library
#include <Servo.h>

// Declare the Servo pin
int servoPin = 9;

// Create a servo object
Servo Servo1;
//char json_msg[]="{\"timeLength\":\"1\",\"speed\":\"5\"}";
int mSpeed=5;
int tLength=5;
//DynamicJsonDocument doc(1024);
String aSpeed="";

void setup() {
  
    // We need to attach the servo to the used pin number
    Servo1.attach(servoPin);

    // initialize digital pin LED_BUILTIN as an output.
    pinMode(LED_BUILTIN, OUTPUT);
 
    Serial.begin(115200); 
}




void loop () {

  //Read in from the computer
  aSpeed=Serial.readString();
  mSpeed=aSpeed.toInt();
  Serial.println(aSpeed);
  
  //json_msg=Serial.readString();
  //deserializeJson(doc, json);  
  //mSpeed=doc["speed"]
  //tlength=doc["timeLength"]  
  //Serial.println(json_msg);
  
   // Make servo go to 0 degrees
    Servo1.write(0);
    digitalWrite(LED_BUILTIN, LOW);   // turn the LED off by making the voltage LOW
    delay(7000);                      // wait for 7 seconds
   // Make servo go to 90 degrees
    //Servo1.write(80);
    Servo1.write(mSpeed);
    digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)
    delay(7000);                      // wait for 7 seconds

   // Make servo go to 180 degrees
    //Servo1.write(180);
   //delay(10000);


 //  Serial.println(millis());
 //  Serial.print(__TIME__);
  
}
