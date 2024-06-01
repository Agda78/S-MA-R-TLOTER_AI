#include <math.h>

float pi = 3.14;

double theta = pi * 0.0625;

int i = 0;


void setup() {
  // Inizializza la comunicazione seriale alla velocità di trasmissione di 9600 baud
  Serial.begin(9600); 
}

void loop() {
  float dato = sin(2 * theta * i);
  // Invia il valore letto tramite la porta seriale
  Serial.println(dato);
  // Attende 100 millisecondi
  i++;
  delay(100); 
}
