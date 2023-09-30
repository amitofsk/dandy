//Reference:https://forum.arduino.cc/t/creating-your-own-pwm-to-control-a-servo/129869/8

//This needs debugging. As of now, it basically is just the example from the ref above. 

int servo = 9;
int led=13; 
void setup() { 
  
  pinMode(servo, OUTPUT); //OUTPUT setup
  pinMode(led, OUTPUT);
 

  for ( int i = 0; i < 5; i++){ // Set the possition to 90 degrees
   digitalWrite(servo, HIGH);
    delayMicroseconds(1500);
    digitalWrite(servo, LOW);
  
  }
  
  
  delay(2000);
  
} 
 
 
void loop() {
  for (int j=0;j<5;j++)
    {
 
    for ( int i = 0; i < 50; i++){
      digitalWrite(led, HIGH);
      digitalWrite(servo, HIGH);
      delayMicroseconds(1000); // Set the possition to 0 degrees
      digitalWrite(servo, LOW);
      delay(19); 
    }
    for ( int i = 0; i < 50; i++){
      digitalWrite(led, LOW);
      digitalWrite(servo, HIGH);
      delayMicroseconds(2000); //Set the possition to 180 degrees
      digitalWrite(servo, LOW);
      delay(18); 
  }

    } 
}

