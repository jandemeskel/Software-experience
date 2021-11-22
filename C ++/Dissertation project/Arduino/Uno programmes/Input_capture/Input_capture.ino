//---------------------------

volatile unsigned int New_T1, Old_T1, PPS_period ;                                                     
unsigned int pin = 8;                            
bool flag = LOW;
byte prescalar = B01000010;

//---------------------------

ISR(TIMER1_CAPT_vect)                    
{
    New_T1 = ICR1 ;                   
    flag = HIGH;
}

//---------------------------

void setup()
{
  Serial.begin(9600);         
  TCCR1B = prescalar; 
  TIMSK1 = (1<<ICIE1) ;      
  TCCR1A = 0;                                                       
}

//---------------------------

void loop()
{
  if (flag){
    PPS_period =  New_T1 - Old_T1;    
    Old_T1 = New_T1 ;                  
    flag = LOW;    
    Serial.println( PPS_period);   
  }
}
