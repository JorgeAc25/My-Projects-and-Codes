int Pot1=0;
int Pot2=1;
int Pot3=2;

int valorP1;
int valorP2;
int valorP3;

void setup() { 
  Serial.begin(115200);
}

void loop() {
  valorP1=analogRead(Pot1)/4;
  valorP2=analogRead(Pot2)/4;
  valorP3=analogRead(Pot3)/4;

  Serial.print(valorP1);
  Serial.print(" ");
  Serial.print(valorP2);
  Serial.print(" ");
  Serial.println(valorP3);
  delay(100);

  
}
