#include <Arduino.h>
#include <SparkFun_TB6612.h>

const int offsetA = 1;
const int offsetB = 1;

#define AIN1 7
#define BIN1 5
#define AIN2 8
#define BIN2 4
#define PWMA 9
#define PWMB 3
#define STBY 6

Motor motor1 = Motor(AIN1, AIN2, PWMA, offsetA, STBY);
Motor motor2 = Motor(BIN1, BIN2, PWMB, offsetB, STBY);



void setup() {
  forward(motor1, motor2, 255);
  delay(2000);
  right(motor1, motor2, 255);
  delay(2000);
  forward(motor1, motor2, 255);
}

void loop() {
  // put your main code here, to run repeatedly:
}
