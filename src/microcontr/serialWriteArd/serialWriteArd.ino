//Connect a button between pin 8 and 3.3V power.
//When you press the button, the internal LED turns on, and 'T' is printed.
//Otherwise 'F' is printed.

int button=8;
int led=13;
int buttonState=0;
void setup() {  
  Serial.begin(115200);
  Serial.println("hi");  
  pinMode(button, INPUT);
  pinMode(led, OUTPUT);
}

void loop() {
  buttonState=digitalRead(button);
  if (buttonState == HIGH) {
       digitalWrite(led, HIGH);
       Serial.println("T");
     } 
   else {
     digitalWrite(led, LOW);
     Serial.println("F");
   }
   delay(1000);  
}
