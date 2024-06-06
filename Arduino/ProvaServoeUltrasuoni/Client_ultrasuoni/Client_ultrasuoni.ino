#include <ESP8266WiFi.h>

const char* ssid = "SSID_RETE";
const char* password = "PASSWORD_RETE";

const char* server_ip = "192.168.1.115";  // IP address del server Python
const uint16_t server_port = 8080;

const int trigPin = D1;
const int echoPin = D2;
long duration;
int distance;

WiFiClient client;

void setup() {
  Serial.begin(115200);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected.");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  // Misura la distanza
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2;

  // Invia la distanza al server se supera una certa soglia (ad esempio, 10 cm)
  if (distance < 10) {
    if (client.connect(server_ip, server_port)) {
      String message = "Distance: " + String(distance) + " cm";
      client.println(String(distance));
      client.stop();
      Serial.println(message);
    }
  }

  delay(1000);  // Attendi un secondo prima di effettuare una nuova misurazione
}
