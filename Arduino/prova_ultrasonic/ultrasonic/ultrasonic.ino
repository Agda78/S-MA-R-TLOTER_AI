#define   ECHO_PIN    26
#define   TRIG_PIN    25
#define   DIM         10


float duration, distance;
float distance_vector [DIM];

float media(float * vettore){
  float temp;
  for(int i=0; i<DIM; i++){
    temp += vettore[i];
  }
  return (temp/DIM);
}

void setup() {
  // put your setup code here, to run once:
  pinMode(ECHO_PIN, INPUT); 
  pinMode(TRIG_PIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  for(int i=0; i<10; i++){
    digitalWrite(TRIG_PIN, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIG_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG_PIN, LOW);
  
    
    duration = pulseIn(ECHO_PIN, HIGH);
    distance = (duration*.0343)/2;
    
    distance_vector[i] = distance;
  }
  distance = media(distance_vector);
  Serial.print("Distanza in cm: ");
  Serial.println(distance);
  delay(1000);
  distance = 0;
}
