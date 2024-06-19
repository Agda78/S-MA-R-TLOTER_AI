#include <WiFi.h>
#include "ESP32Servo.h"


#define   SERVO_PIN   33
#define   ECHO_PIN    26
#define   TRIG_PIN    25
#define   DIM         10

float distanza;
Servo myservo;
int pos = 90;

// Configurazione della rete Wi-Fi
const char* ssid     = "TIM-45442572";
const char* password = "fdDEA6XGFZxttkH93xH9cd4U";

// Configurazione del server
const char* serverIP = "192.168.1.24";  // Indirizzo IP del server
const uint16_t serverPort = 5050;       // Porta del server
const uint16_t servo_port = 80;

WiFiClient client;
WiFiServer server(80);

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
  if (distanza < 10){
    if (!client.connect(serverIP, serverPort)) {
      Serial.println("Connection to server failed");
      return;
      }
    client.write((uint8_t)1);
    Serial.println("Rilevazione comunicata");
    client.stop(); //chiusura connessione
    //attesa del comando da dare al SERVO

    
    server.begin();
    Serial.printf("Server started on port %d\n", serverPort);

    
    // Controlla se il client (processo_b) è connesso
    WiFiClient process_b = server.available();
  
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
      // Leggi l'intero su 8 bit (byte)
      //uint8_t receivedValue = process_b.read();
      
      //Serial.print("Received value: ");
      //Serial.println(receivedValue);
      //servo_rotation((int)receivedValue);
      }
    }
    client.stop();
    Serial.println("Client disconnected");
   
  }

  delay(2000);
}
