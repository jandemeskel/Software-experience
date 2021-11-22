volatile unsigned int New_C1, Old_C1, C1_count, New_C2, Old_C2, C2_count;                                                  
 unsigned int pin_C1 = 48, pin_C2 = 49;                            
 bool flag_C1 = LOW, flag_C2 = LOW;
 byte prescalar = B01000010;   // B01000001 = No prescalar, B01000010 = 256 prescalar
 
// --------------------------------------------------
//Interrupt service routines for timer counters 5 & 4
//---------------------------------------------------

ISR(TIMER5_CAPT_vect)
{   
    New_C1 = ICR5 ;                    
    flag_C1 = HIGH;              
}
ISR(TIMER4_CAPT_vect)
{
  New_C2 = ICR4 ;
  flag_C2 = HIGH;
}

// ----------------------------------
//Timer register setup (writing bits)
//-----------------------------------

void setup()
{
  Serial.begin(9600); 
       
  TCCR5B = prescalar;
  TIMSK5 = (1<<ICIE5) ;      
  TCCR5A = 0;     
 
  TCCR4B = prescalar;
  TIMSK4 = (1<<ICIE4);
  TCCR4A = 0;
}

// -----------------------------
// Repeat instructions after ISR
// -----------------------------

void loop(){ 
  if (flag_C1)
  {
    C1_count = New_C1 - Old_C1;
    Old_C1 = New_C1;

    flag_C1 = LOW;
    Serial.println( "Clock 1 count is");
    Serial.println( C1_count);  
  }

  if (flag_C2)
  {
    C2_count = New_C2 - Old_C2;
    Old_C2 = New_C2;

    flag_C2 = LOW;  
    Serial.println( "Clock 2 count is");
    Serial.println(C2_count);
    Serial.println();
  }
}

//seperate flags, to stop cross triggering
