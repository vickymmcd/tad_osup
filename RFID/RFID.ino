#import "RFID.h"

void setup() {
  // put your setup code here, to run once:
  setup_prox();
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  int cardCode = read_prox();
  if (cardCode != 0) {
    Serial.println(cardCode);
  }
//  Serial.println(analogRead(A0));
}
