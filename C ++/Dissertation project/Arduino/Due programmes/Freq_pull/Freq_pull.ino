
int bitvalue;
int deltaf = 0;

void setup() {
  //put your setup code here, to run once:
  analogWriteResolution(12);
  //i = 1;
}

void loop() {
  //put your main code here, to run repeatedly:
  if (deltaf>150){
    deltaf = 150;
    analogWrite(DAC1, 4096);
  };
  if (deltaf<-150){
    deltaf = -150;
    analogWrite(DAC1, 4096);
  };
  if (-150<deltaf<150){
    analogWrite(DAC1, 0);
  };
  bitvalue = -deltaf*(2048/150);
  analogWrite(DAC0, 2047+bitvalue);
  //int j = i * 100;
  //analogWrite(DAC0, j);
  //i = i + 1;
}
