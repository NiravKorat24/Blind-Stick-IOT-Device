
#define TRIG_PIN 9
#define ECHO_PIN 10
#define BUZZER_PIN 8

long duration;
int distance;

void setup() {
  Serial.begin(9600);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(BUZZER_PIN, OUTPUT);
}

void loop() {

  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  duration = pulseIn(ECHO_PIN, HIGH, 60000);  
  distance = duration * 0.034 / 2;           

  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  if (distance > 0 && distance < 30) {
    digitalWrite(BUZZER_PIN, HIGH);  
  } else {
    digitalWrite(BUZZER_PIN, LOW);  
  }

  delay(300);
}
