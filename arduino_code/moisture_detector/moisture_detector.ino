const int airValue = 490;
const int waterValue = 290;
int intervals = (airValue - waterValue)/3;
int soilMoistureValue = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  soilMoistureValue = analogRead(0);
  if (soilMoistureValue > waterValue && soilMoistureValue < (waterValue + intervals)) {
    Serial.print("Very wet:");
    Serial.print(soilMoistureValue);
  } else if (soilMoistureValue > (waterValue + intervals) && soilMoistureValue < (airValue - intervals)) {
    Serial.println("Wet:");
    Serial.print(soilMoistureValue);
  } else if (soilMoistureValue < airValue && soilMoistureValue > (airValue - intervals)) {
    Serial.println("Dry:");
    Serial.print(soilMoistureValue);
  }
  delay(100);
}