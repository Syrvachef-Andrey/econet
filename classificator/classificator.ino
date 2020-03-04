#include <NewPing.h>
#define PIN_TRIG 12
#define PIN_ECHO 11
#define IN3 8
#define IN2 7
#define MAX_DISTANCE 200
int chvet2 = 0;
int chvet3 = 0;
unsigned int distance = 0;
NewPing sonar(PIN_TRIG, PIN_ECHO, MAX_DISTANCE);
void setup() {

  Serial.begin(9600);
  pinMode(IN2 , INPUT);
  pinMode(IN3, INPUT);
}
void Ultrasonicc() {
  unsigned int distance = sonar.ping_cm();
  Serial.print(distance);
  Serial.print("cm");
  Serial.print("\t");
}
void color() {
  chvet2 = digitalRead(IN2);
  chvet3 = digitalRead(IN3);
  Serial.print(chvet2);
  Serial.print("\t");
  Serial.println(chvet3);
}
void plastik() {
  if ( distance < 20 && chvet3 == 1 && chvet2 == 1)
  {
    Serial.println("Plastik");
  }
}
void metalik() {
  if ( distance < 20 && chvet3 == 0 && chvet2 == 0)
  {
    Serial.println("Metalik");
  }
}
void bumaga() {
  if ( distance < 20 && chvet3 == 1 && chvet2 == 0)
  {
    Serial.println("bumaga");
  }
}

void loop() {
  delay(300);
  color();
  Ultrasonicc();
  bumaga();
  metalik();
  plastik();

}
