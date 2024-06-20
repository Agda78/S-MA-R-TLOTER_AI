#include <SPI.h>
#include <WiFi.h>
#include "ESP32Servo.h"
//#include <esp_system.h>

#define   SERVO_PIN   33
#define   ECHO_PIN    26
#define   TRIG_PIN    25
#define   DIM         10

float distanza;
Servo myservo;
int pos = 90;

// Configurazione della rete Wi-Fi
const char* ssid     = "SmartLoter";
const char* password = "FNS1926!";

// Configurazione del server
const char* serverIP = "192.168.188.2";  // Indirizzo IP del server
const uint16_t serverPort = 5050;       // Porta del server
const uint16_t servo_port = 6060;

WiFiClient client;
WiFiServer server(serverPort);

float rileva(){
  float duration, distance;
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  duration = pulseIn(ECHO_PIN, HIGH);
  distance = (duration*.0343)/2;
  return distance;
}

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

void server_servo(){
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
    Serial.println("Process_b acquisito.");
    while (process_b.connected()) {
      if (process_b.available()) {
        int incomingInt = process_b.parseInt();
        Serial.print("Received integer: ");
        Serial.println(incomingInt);
        servo_rotation((uint8_t)incomingInt);
        client.stop();
      }
    }
  }
}
void setup() {
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
  
  
  pinMode(ECHO_PIN, INPUT); 
  pinMode(TRIG_PIN, OUTPUT);

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
  Serial.println("InizioCIclo");
  distanza = rileva();
  if (distanza < (float)10){
    while (!client.connect(serverIP, servo_port)) {
      Serial.println("Connection to server failed");
      //return;
      }
    client.write((uint8_t)1);
    Serial.println("Rilevazione comunicata");
    client.stop(); //chiusura connessione
    //attesa del comando da dare al SERVO

    server_servo();
    
    }
    Serial.println("Client disconnected");
    delay(1000);
  }
