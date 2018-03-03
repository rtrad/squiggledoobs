

#include "MeOrion.h"
#include <SoftwareSerial.h>
#include <Wire.h>
#include <stdint.h>

int device_id = 0;

MePIRMotionSensor PIRmotion_val(PORT_3);

MeRGBLed led(PORT_4);

MeBluetooth bluetooth(PORT_5);

MeSoundSensor mySound(PORT_6);

// MeUltrasonicSensor ultraSensor(PORT_7);


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
  if(detected) {
    person();
  } 
  prev_detected = detected;

  delay(100);

  
}
/**
 * A person has been detected
 * Add to counter
 * send bluetooth data
 * how busy is a pass
**/
void person() {

  blink();
  String out = "";
  out += mySound.strength();

  bluetooth.println(out);
  
}
void blink() {
  uint8_t r = 250;

  led.setColorAt(0, r, 0,0);
  led.show();
}

