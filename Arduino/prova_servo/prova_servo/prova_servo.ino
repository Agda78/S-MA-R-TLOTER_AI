#include "ESP32Servo.h"
#define   SERVO_PIN   33

Servo myservo;
int pos = 90; //variabile utile per conservare l'informazione sulla posizione


void setup() {
  // put your setup code here, to run once:
  //Allocazione dei timer
  ESP32PWM::allocateTimer(0);
  ESP32PWM::allocateTimer(1);
  ESP32PWM::allocateTimer(2);
  ESP32PWM::allocateTimer(3);

  //standard 50hz servo
  myservo.setPeriodHertz(50);
  myservo.attach(SERVO_PIN, 500, 2400);
}

void loop() {
  // put your main code here, to run repeatedly:
  for(pos=90; pos<=180; pos+=1){
    myservo.write(pos);
    delay(15);
  }
  delay(1000);
  for(pos=180; pos>=90; pos-=1){
    myservo.write(pos);
    delay(15);
  }
  delay(1000);
  for(pos=90; pos>=0; pos-=1){
    myservo.write(pos);
    delay(15);
  }
  delay(1000);
  for(pos=0; pos<=90; pos+=1){
    myservo.write(pos);
    delay(15);
  }
  delay(1000);

}
