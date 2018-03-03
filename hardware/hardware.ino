

#include "MeOrion.h"
#include <SoftwareSerial.h>
#include <Wire.h>
#include <stdint.h>

int device_id = 0;

MeRGBLed led(PORT_3);

MePIRMotionSensor PIRmotion_val(PORT_6);

MeBluetooth bluetooth(PORT_5);

String test = "test out";

bool detected = 0;
bool prev_detected = 0;

void setup() {

  Serial.begin(115200);
  bluetooth.begin(115200);    //The factory default baud rate is 115200
}

void loop() {
  led.setColorAt(0,0,0,0);
  led.show();
  detected = PIRmotion_val.isHumanDetected();
  if(detected ) {
    color();
    sendBTData();
  }
  prev_detected = detected;

  delay(100);

  
}
void sendBTData() {
  bluetooth.println(device_id);
  
}
void color() {
  uint8_t r = 250;

  led.setColorAt(0, r, 0,0);
  led.show();
}

