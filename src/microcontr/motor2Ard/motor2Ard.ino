/*
This example doesn't work. It still needs a lot of development. 

Here's the example I'm trying for... Assume a small servo motor is wired
to an Arduino. The Arduino is connected to the computer by USB cable. A Python
program on the computer lets a user spin a dial and send a corresponing
float value, ending in the character X, to the microcontroller. 
The microcontroller uses this value to set the motor speed, and the motor
spins forward and back.

This example would require the user to do two things almost simultaneously.
The first thing would be to read characters from the USB cable and the second
is to spin the motor. 

Arduinos don't have multiple processors or allow multithreading. In Python, 
CircuitPython, and MicroPython, the asyncIO library lets you do two tasks
almost simultaneously. Arduino doesn't have asyncIO. It does, however, 
have a library called protothreads. 

Here's my reference for the protothread library:
https://roboticsbackend.com/arduino-protothreads-tutorial/

In this example, I try to use protothreads for this purpose.
Parts of this example closely follow the reference above.
I was able to get multiple protothreads started. However,
this example still needs a lot more development before it actually
does what it should.

*/


#include <pt.h>
#define led LED_BUILTIN
#define servo 9


// Declare 3 protothreads
static struct pt pt1, pt2, pt3;

// First protothread function to blink LED 1 every 1 second
static int protothreadUseSerial(struct pt *pt)
{
  static unsigned long lastTimeBlink = 0;
  PT_BEGIN(pt);
  Serial.println("Use Serial Thread");
  //protothreadSpinMotor(&pt3);
  while(1) {
    lastTimeBlink = millis();
    PT_WAIT_UNTIL(pt, millis() - lastTimeBlink > 1000);
    digitalWrite(led, HIGH);
    lastTimeBlink = millis();
    PT_WAIT_UNTIL(pt, millis() - lastTimeBlink > 1000);
    digitalWrite(led, LOW);
  }
  PT_END(pt);
}

// Second protothread function to blink LED 2 every 0.5 second
static int protothreadCheckSerial(struct pt *pt)
{
  static unsigned long lastTimeBlink = 0;
  PT_BEGIN(pt);
  Serial.println("Check Serial Thread");
  /*
  while(1) {
    lastTimeBlink = millis();
    PT_WAIT_UNTIL(pt, millis() - lastTimeBlink > 500);
    digitalWrite(LED_2_PIN, HIGH);
    lastTimeBlink = millis();
    PT_WAIT_UNTIL(pt, millis() - lastTimeBlink > 500);
    digitalWrite(LED_2_PIN, LOW);
  }
  */
  PT_END(pt);
}

// Third protothread function to power on LED 3 if
// the push button is pressed.
static int protothreadSpinMotor(struct pt *pt)
{
  static unsigned long startTime = 0;
  static double pulse_high_us=0;
  static int pulse_period_us=1500;
  PT_BEGIN(pt);
  Serial.println("Spin Motor Thread");
  for (int j=0; j< 100; j++)
  {
    startTime=millis();
    pulse_high_us=1.0*pulse_period_us*j/30;
    digitalWrite(servo, HIGH);
    PT_WAIT_UNTIL(pt, millis()-startTime>(0.001*pulse_high_us));
    digitalWrite(servo, LOW);
    PT_WAIT_UNTIL(pt, millis()-startTime>(0.001*pulse_period_us));
    
  }
  PT_END(pt);
}

// In setup, set all LEDs as OUTPUT, push button as INPUT, and
// init all protothreads
void setup() {
  pinMode(led, OUTPUT);
  pinMode(servo, OUTPUT);
  PT_INIT(&pt1);
  PT_INIT(&pt2);
  PT_INIT(&pt3);
}

// In the loop we just need to call the protothreads one by one
void loop() {
  protothreadUseSerial(&pt1);
 // protothreadCheckSerial(&pt2);
  protothreadSpinMotor(&pt3);
}
