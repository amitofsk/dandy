/*
Now with protothreads?..
Refs:
https://roboticsbackend.com/arduino-protothreads-tutorial/

Sketch->Include Libraries -> Manage Library -> Add the protothreads library
*/
#include <pt.h>

int servo=0;
int led=13;
static struct pt pt1, pt2, pt3;

double steps=50;
int pulse_period_us=1500;
double pulse_high_us=0.0; 


static int protothreadUseSerial(struct pt *pt)
{
   static unsigned long lastTimeBlink = 0;
  PT_BEGIN(pt);
  Serial.println("Started UseSerial");
  while(1) {
    lastTimeBlink = millis();
    PT_WAIT_UNTIL(pt, millis() - lastTimeBlink > 1000);
    digitalWrite(led,  HIGH);
    lastTimeBlink = millis();
    PT_WAIT_UNTIL(pt, millis() - lastTimeBlink > 1000);
    digitalWrite(led, LOW);
    protothreadSpinMotor(&pt3, 50);
  }
  PT_END(pt);
}

static int protothreadCheckSerial(struct pt *pt)
{
  static unsigned long lastTimeBlink = 0;
  PT_BEGIN(pt);
  Serial.println("Started CheckSerial");
  PT_END(pt);
  
}

static int protothreadSpinMotor(struct pt *pt, int mySteps)
{
  
  PT_BEGIN(pt);
     Serial.println("Started SpinMotor");
     int steps;
     //steps=mySteps;
     steps=50;
     //Spin forward  
     Serial.println("Forward");   
     digitalWrite(led, HIGH);
     for ( int j = 0; j < steps; j++){
          //The variable jj sweeps from 0 to steps, and keeps track of which step we are on. 
          //The 1.0 is needed in the next line to ensure double computation, not int.
          pulse_high_us=1.0*pulse_period_us*j/steps;
          digitalWrite(servo, HIGH);
          delayMicroseconds(pulse_high_us);    
          digitalWrite(servo, LOW);
          delayMicroseconds(pulse_period_us-pulse_high_us);
          delay(150); //delay 0.15 seconds between steps
     }//close the for over j
     
     //Spin backwards.
     Serial.println("Back");
     digitalWrite(led, LOW);
     //delay(1000);
     for(int j=0; j< steps; j++) {
       pulse_high_us=1.0*pulse_period_us*j/steps;
       digitalWrite(servo, HIGH);
       delayMicroseconds(pulse_period_us-pulse_high_us);
       digitalWrite(servo, LOW);
       delayMicroseconds(pulse_high_us);
       delay(150);
    }//close the for over j
  
  PT_END(pt);
  
}

void setup() {

  Serial.begin(115200);
  pinMode(servo, OUTPUT); 
  pinMode(led, OUTPUT);
  
  PT_INIT(&pt1);
  PT_INIT(&pt2);
  PT_INIT(&pt3);
}


void loop () {
  //protothreadCheckSerial(&pt1);
  protothreadUseSerial(&pt2);
  //protothreadSpinMotor(&pt3, 50);
}
