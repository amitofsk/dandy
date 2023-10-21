/*
 This example spins a motor back and forth at five different speeds.
 Start with a small servo motor that can be powered from the Arduino.
 Connect the brown motor wire to Arduino's GND. Connect the red motor wire to 
 Arduino's 5V. Connect the yellow motor wire to Arduino's pin 9.
 Reference:https://forum.arduino.cc/t/creating-your-own-pwm-to-control-a-servo/129869/8
*/
int servo = 9;
int led=13; 

void setup() { 
  //All instructions are in setup(), not loop(), because we only want the motor to spin a finite number of times. 
  pinMode(servo, OUTPUT); 
  pinMode(led, OUTPUT);
  //Steps represents the steps taken to go between two angles 180 degrees apart.
  double steps=50;
  //We're bit banging PWM as opposed to using a library or any built in pwm functions. 
  //We're using signals with a period of 1500 microseconds which corresponds to a frequency of 667Hz.
  int pulse_period_us=1500;
  //The motor angle is controlled by duty cycle. The  variable pules_high_us
  //represents the time in microseconds that the pulse is high.
  //The pwm duty cycle is given by pulse_high_us/pulse_period_us. 
  //duty cycle of 0 corresponds to one angle. Duty cycle of 1 is an angle 180 degrees away from it.
  double pulse_high_us=0.0; 
 
  //We'll spin the motor at 5 speeds, determined by the number of steps.
  //Why does steps influence speed?
  //We're going between two angles in the number of steps specified. We spend 0.15s at each step. 
  //For example, if we take 30 steps to go between 0 and 180 degrees, 
  //with 0.15s between steps, this process takes 30*0.15=4.5s.
  //For example, if we take 110 steps with 0.15s between steps, this process takes 16.5s.
  //Why use steps instead of pulse_period to set the motor speed?
  //We want observable speeds. If we just altered pulse_period, the motor would spin too fast to be observable.
  for (int ii=1;ii<5;ii++)
    {
     //The variable ii sets the number of steps, and hence speed of going between the angles. 
     steps=20*ii+10;
     //Spin forward     
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
     digitalWrite(led, LOW);
     delay(1000);
     for(int j=0; j< steps; j++) {
       pulse_high_us=1.0*pulse_period_us*j/steps;
       digitalWrite(servo, HIGH);
       delayMicroseconds(pulse_period_us-pulse_high_us);
       digitalWrite(servo, LOW);
       delayMicroseconds(pulse_high_us);
       delay(150);
    }//close the for over j
 } //close the for over ii
}//close the setup 
 
 
void loop() {
 
}
