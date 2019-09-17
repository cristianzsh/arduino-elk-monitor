#include "DHT.h"
 
#define DHTPIN A1
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

int PinA0 = A0;

void setup() {
    Serial.begin(9600);
    pinMode(PinA0, INPUT);
    dht.begin();
}

void loop() {
    float h = dht.readHumidity();
    float t = dht.readTemperature();

    if (isnan(t) || isnan(h)) {
        Serial.println("Failed to read from DHT!");
    } else {
        int g = analogRead(PinA0);
        
        Serial.print(h);
        Serial.print(" ");
        Serial.print(t);
        Serial.print(" ");
        Serial.println(g);
    }
    
    delay(15000);
}
