int pin = 49;
unsigned long duration_HIGH, duration_LOW, duration;

void setup()
{
  Serial.begin(9600);
  pinMode(pin, INPUT);
 
}

void loop()
{
 duration_HIGH = pulseIn(pin,HIGH, 10000000);
 duration_LOW = pulseIn(pin,LOW, 10000000);

 duration = duration_HIGH + duration_LOW;

 Serial.println(" time interval between PPS signals is:");
 Serial.println(duration);
}
