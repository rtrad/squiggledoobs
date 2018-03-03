

#include "MeOrion.h"
#include <SoftwareSerial.h>
#include <Wire.h>
#include <stdint.h>


MeRGBLed led(PORT_3);

MePIRMotionSensor PIRmotion_val(PORT_6);

bool detected = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  led.setColorAt(0,0,0,0);
  led.show();
  detected = PIRmotion_val.isHumanDetected();
  if(detected) {
    color();
  }

  Serial.print(detected);

  delay(100);
}

void color() {
  uint8_t r = 250;

  led.setColorAt(0, r, 0,0);
  led.show();
}

