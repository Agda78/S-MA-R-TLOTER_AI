// Definizione del pin del LED
const int ledPin = 13;

void setup() {
  // Inizializzazione del pin del LED come output
  pinMode(ledPin, OUTPUT);
  // Inizializzazione della comunicazione seriale
  Serial.begin(9600);
  // Inizializzazione del generatore di numeri casuali
  randomSeed(analogRead(0));
}

void loop() {
  // Controlla se ci sono dati disponibili sulla seriale
  if (Serial.available() > 0) {
    // Legge i dati dalla seriale
    String command = Serial.readStringUntil('\n');
    command.trim();  // Rimuove eventuali spazi bianchi dai dati ricevuti

    // Controlla il comando ricevuto e agisce di conseguenza
    if (command == "ON") {
      digitalWrite(ledPin, HIGH);
      Serial.println("LED acceso");
    } else if (command == "OFF") {
      digitalWrite(ledPin, LOW);
      Serial.println("LED spento");
    } else if (command == "GET") {
      int randomNumber = random(0, 100);  // Genera un numero casuale tra 0 e 99
      Serial.println(randomNumber);
    } else {
      Serial.println("Comando non riconosciuto");
    }
  }
  delay(100);
}
