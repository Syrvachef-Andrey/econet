#include <NewPing.h>
#define PIN_TRIG 12
#define PIN_ECHO 11
#define IN3 8
#define IN2 7 
#define MAX_DISTANCE 200 
int chvet2 = 0;
int chvet3 = 0;
NewPing sonar(PIN_TRIG, PIN_ECHO, MAX_DISTANCE);
void setup() {

  Serial.begin(9600);
  pinMode(IN2 , INPUT);
  pinMode(IN3, INPUT);
}
void Maslovlox(){
    unsigned int distance = sonar.ping_cm();
  Serial.print(distance);
  Serial.println("cm");
   if(distance <= 15)
  {
    Serial.println("Maslov loshara");
  }
}


void loop() {
  //Maslovlox();
  delay(500);
  chvet2 = digitalRead(IN2);
  chvet3 = digitalRead(IN3);
  Serial.print(chvet2);
  Serial.print("\t");
  Serial.println(chvet3);
  

}
