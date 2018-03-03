

#include "MeOrion.h"
#include <SoftwareSerial.h>
#include <Wire.h>
#include <stdint.h>


MeRGBLed led(PORT_3);

MePIRMotionSensor PIRmotion_val(PORT_6);

MeBluetooth bluetooth(PORT_5);

unsigned char table[128] = {0};

bool detected = 0;

void setup() {

  Serial.begin(115200);
  bluetooth.begin(115200);    //The factory default baud rate is 115200
  Serial.println("Bluetooth Start!");
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

