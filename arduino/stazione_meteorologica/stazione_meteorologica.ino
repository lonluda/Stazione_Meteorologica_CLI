#include <DHT.h>
#include <Wire.h>

double hum;           // Variabile in cui verrà inserita la percentuale di umidità
double temp;          // Variabile in cui verrà inserita la temperatura
DHT dht(2, 22);       // Imposta il PIN di interrogazione del sensore DHT22 e specifica il modello di sensore 22 = DHT22

void setup() {
  // put your setup code here, to run once:                     
  Serial.begin(9600); // Inizializzazione Comunicazione Seriale
  dht.begin();        // Inizializzazione DHT
  pinMode(11, OUTPUT);  // Stato
  digitalWrite(11, HIGH); // sets the digital pin 13 on
}

void loop() {
  // put your main code here, to run repeatedly:
     hum = dht.readHumidity();         // Richiesta valore HUM da DHT22 espressa in %
     temp = dht.readTemperature();     // Richiesta valore TEMP da DHT22 espresso in °C
      Serial.println(temp);
      Serial.println(hum);
      Serial.println(1024);
  delay(2000);
}
