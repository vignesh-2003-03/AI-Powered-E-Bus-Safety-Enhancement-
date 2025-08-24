#include <SoftwareSerial.h>
#include <LiquidCrystal.h>

LiquidCrystal lcd(8, 9, 10, 11, 12, 13);

int buz_status;

int trans_dat;

#define m1 3
#define m2 4
#define en1 5

#define BUZZER_PIN 6
#define BUZZER_OFF_PIN 7
#define LED1 2
#define LED2 7

long BUZZER_OFF_DELAY = 5000; // Time in milliseconds (adjust as needed)

unsigned long buzzerOffTime = 0;
unsigned long sendInterval = 10000; // Send data every 10 seconds
unsigned long lastSendTime = 0;

#define python Serial
#define splash splash1

void setup() {
Serial.begin(115200);

LcDSet();
pinMode(BUZZER_PIN, OUTPUT);
pinMode(BUZZER_OFF_PIN, OUTPUT);
pinMode(LED1, OUTPUT);
pinMode(LED2, OUTPUT);
pinMode(m1, OUTPUT);
pinMode(m2, OUTPUT);
analogWrite(en1, 0);
digitalWrite(m1, LOW);
digitalWrite(m2, LOW);
// Initially, turn off both the buzzer and the buzzer off pin
digitalWrite(BUZZER_PIN, LOW);
digitalWrite(BUZZER_OFF_PIN, LOW);
digitalWrite(LED1, LOW);
digitalWrite(LED2, LOW);
}

void LcDSet() {
lcd.begin(16, 2);

splash(0, "EYE MOTION");
splash(1, "");

delay(2000);
lcd.clear();
}

void loop() {

delay(100);
// Check if it's time to send trans_data
if (millis() - lastSendTime >= sendInterval) {


// Perform actions to update trans_data as needed
if (trans_dat == 1) {
analogWrite(en1, 100);
}
if (trans_dat == 2) {
analogWrite(en1, 0);
digitalWrite(m1, LOW);
digitalWrite(m2, LOW);
}
if (trans_dat == 3) {
analogWrite(en1, 255);
digitalWrite(m1, HIGH);
digitalWrite(m2, LOW);
}
lastSendTime = millis();
}

if (trans_dat == 1) {
analogWrite(en1, 100);
}
if (trans_dat == 2) {
analogWrite(en1, 0);
digitalWrite(m1, LOW);
digitalWrite(m2, LOW);
}
if (trans_dat == 3) {
analogWrite(en1, 255);
digitalWrite(m1, HIGH);
digitalWrite(m2, LOW);
}

while (python.available() > 0) {
String receivedData = python.readStringUntil('\n');
processMessage(receivedData);
splash(1, receivedData);
}

// Check if it's time to turn off the buzzer
if (millis() - buzzerOffTime >= BUZZER_OFF_DELAY) {
if (trans_dat == 1 && buz_status == 0) {
digitalWrite(BUZZER_PIN, HIGH);
digitalWrite(LED1, HIGH);
digitalWrite(LED2, HIGH);
buz_status = 1;
BUZZER_OFF_DELAY = 50;
} else if (trans_dat == 2 && buz_status == 0) {
digitalWrite(BUZZER_PIN, HIGH);
digitalWrite(LED1, HIGH);
delay(10);
digitalWrite(LED1, LOW);
digitalWrite(LED2, HIGH);
delay(10);
digitalWrite(LED2, LOW);
buz_status = 1;
trans_dat = 2;
BUZZER_OFF_DELAY = 5000000;
} else if (buz_status) {
digitalWrite(BUZZER_PIN, LOW);
digitalWrite(LED1, LOW);
digitalWrite(LED2, LOW);
buz_status = 0;
}
buzzerOffTime = millis();
}
}

void processMessage(String data) {
data.trim();

if (data != "drowsy" && data != "alert" && data != "rst" && data != "run") {
return;
}

python.println("Received: " + data);

if (data == "run") {
digitalWrite(BUZZER_PIN, LOW);
digitalWrite(LED1, LOW);
digitalWrite(LED2, LOW);
trans_dat = 3;
buz_status = 0;
BUZZER_OFF_DELAY = 100;
buzzerOffTime = millis();
} else if (data == "drowsy") {
digitalWrite(BUZZER_PIN, HIGH);
digitalWrite(LED1, HIGH);
digitalWrite(LED2, HIGH);
trans_dat = 2;
buz_status = 1;
BUZZER_OFF_DELAY = 5000000;
buzzerOffTime = millis();
} else if (data == "alert") {
digitalWrite(BUZZER_PIN, HIGH);
digitalWrite(LED1, HIGH);
digitalWrite(LED2, HIGH);
trans_dat = 1;
buz_status = 1;
BUZZER_OFF_DELAY = 100;
buzzerOffTime = millis();
} else if (data == "rst") {
python.println("Resetting...");
delay(1000);
asm volatile(" jmp 0");
}
}
