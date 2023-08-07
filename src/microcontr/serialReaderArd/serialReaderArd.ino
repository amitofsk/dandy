//When the Arduino receives the character `Z` from the computer,
//the internal LED blinks.

int led=13;
char ch;

void setup() {
  Serial.begin(115200);
  Serial.println("hi");
  pinMode(led, OUTPUT);
}

void loop() {
  ch=Serial.read();
  if(ch=='Z')
   {Serial.println(ch);
    digitalWrite(led, HIGH);
    delay(250);
    digitalWrite(led,LOW);
   }

   delay(1000);
}

