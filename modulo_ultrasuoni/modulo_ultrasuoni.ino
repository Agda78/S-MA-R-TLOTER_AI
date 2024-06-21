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
const char* ssid     = "SmartLoter";
const char* password = "FNS1926!";

// Configurazione del server
const char* serverIP = "192.168.188.2";  // Indirizzo IP del server
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
  // put your main code here, to run repeatedly:
  distanza = rileva();
  Serial.print("distanza rilevata: ");
  Serial.println(distanza);
  delay(1000);
}
