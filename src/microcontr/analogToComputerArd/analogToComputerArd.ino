//Voltage divider circuit and A0 ..

const int analogPin=A0;
int aValue=0;
String out_msg="";

void setup() {  
  Serial.begin(115200);
  Serial.println("hi");
}

void loop() {
  aValue=analogRead(analogPin); //values will be 0 to 1023
  out_msg="{\"boardNumber\" : \"2\" , \"boardType\" : \"Arduino\" , \"value\" : \"";
  out_msg=out_msg+aValue;
  out_msg=out_msg+"\"}";
  Serial.println(out_msg);
  delay(1000);
}
