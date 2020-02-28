#include "I2Cdev.h"
#include "MPU6050.h"

#define TO_DEG 57.29577951308232087679815481410517033f
#define T_OUT 20
int in1 = 2;
int in2 = 4;
int in3 = 3;
int in4 = 5;
int enA = 11;
int enB = 10;
MPU6050 accel;

float angle_ax;
long int t_next;

float clamp(float v, float minv, float maxv){
    if( v>maxv )
        return maxv;
    else if( v<minv )
        return minv;
    return v;
}

void setup() {
    
    pinMode(in1,OUTPUT);
    pinMode(in2,OUTPUT);
    pinMode(in3,OUTPUT);
    pinMode(in4,OUTPUT);
    pinMode(enA,OUTPUT);
    pinMode(enB,OUTPUT);
    
    Serial.begin(9600);
    accel.initialize(); // первичная настройка датчика
    Serial.println(accel.testConnection() ? "MPU6050 connection successful" : "MPU6050 connection failed");
}

void loop() {



  
  delay(100);
    long int t = millis();
    if( t_next < t ){
        int16_t ax_raw, ay_raw, az_raw, gx_raw, gy_raw, gz_raw;
        float ay,gx;
        t_next = t + T_OUT;
        accel.getMotion6(&ax_raw, &ay_raw, &az_raw, &gx_raw, &gy_raw, &gz_raw);
        ay = ay_raw / 4096.0;
        ay = clamp(ay, -1.0, 1.0);
        if( ay >= 0){
            angle_ax = 90 - TO_DEG*acos(ay);
        } else {
            angle_ax = TO_DEG*acos(-ay) - 90;
        } 
       Serial.println(angle_ax); // вывод в порт угла поворота вокруг оси X
//        digitalWrite(in1,HIGH);
//        digitalWrite(in2,LOW);
//        digitalWrite(in3,LOW);
//        digitalWrite(in4,LOW);
        
       
       if(angle_ax >= 90)
       {
        Serial.println("stop");
          digitalWrite(in1,LOW);
        digitalWrite(in2,HIGH);
        digitalWrite(in3,LOW);
        digitalWrite(in4,LOW);
        
        analogWrite(enA,0);
       }
      else
       {
        Serial.println("go");
          digitalWrite(in1,LOW);
        digitalWrite(in2,HIGH);
        digitalWrite(in3,LOW);
        digitalWrite(in4,LOW);
        
        analogWrite(enA,90);
       
       }
   }
}
