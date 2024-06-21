#include <WiFi.h>
#include "ESP32Servo.h"



#define   SERVO_PIN   33
#define   ECHO_PIN    26
#define   TRIG_PIN    25

int pos = 90;
Servo myservo;

// Configurazione della rete Wi-Fi
const char* ssid     = "SmartLoter";
const char* password = "FNS1926!";

// Configurazione del server
const char* serverIP = "192.168.188.2";  // Indirizzo IP del server
const uint16_t serverPort = 5050;       // Porta del server
const uint16_t servo_port = 80;

WiFiServer server(serverPort);

void servo_rotation(uint8_t dir){
  if(dir == 0){ //anticlockwise
    for(pos=90; pos<=180; pos+=1){
    myservo.write(pos);
    delay(15);
    }
    delay(2000);
    for(pos=180; pos>=90; pos-=1){
      myservo.write(pos);
      delay(15);
    }
    delay(1000);
  }
  else if(dir == 1){
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
  else {
    Serial.println("VUOTO!");
  }
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP()); 

  //Allocazione dei timer
  ESP32PWM::allocateTimer(0);
  ESP32PWM::allocateTimer(1);
  ESP32PWM::allocateTimer(2);
  ESP32PWM::allocateTimer(3);
  
  //standard 50hz servo
  myservo.setPeriodHertz(50);
  myservo.attach(SERVO_PIN, 500, 2400);

}

void server_foo();

void loop() {
  // put your main code here, to run repeatedly:
  server_foo();
  delay(1500);
}

void server_foo(){
  server.begin();
  Serial.printf("Server started on port %d\n", serverPort);
  WiFiClient process_b;
  //do{
    //process_b = server.available();
  //}while(process_b == NULL);
  while(!process_b){
    process_b = server.available();
  }
  Serial.println("debug");
  delay(100);
   if (process_b) {
      Serial.println("processo_b connected");
      
      while (process_b.connected()) {
        // Verifica se ci sono dati disponibili
        if (process_b.available()) {
          // Leggi l'intero su 8 bit (byte)
          uint8_t receivedValue = process_b.read();
          
          Serial.print("Received value: ");
          Serial.println(receivedValue);
          servo_rotation((int)receivedValue);
          
        }
      }
   }
}
