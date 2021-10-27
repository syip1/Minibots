#include <Arduino.h>
#include <SparkFun_TB6612.h>

const int offsetA = 1;
const int offsetB = 1;

#define AIN1 2
#define BIN1 7
#define AIN2 4
#define BIN2 6
#define PWMA 3
#define PWMB 5
#define STBY 9

Motor motor1 = Motor(AIN1, AIN2, PWMA, offsetA, STBY);
Motor motor2 = Motor(BIN1, BIN2, PWMB, offsetB, STBY);

void setup() {
  motor1.drive(255,1000);
}

void loop() {
  // put your main code here, to run repeatedly:
}
