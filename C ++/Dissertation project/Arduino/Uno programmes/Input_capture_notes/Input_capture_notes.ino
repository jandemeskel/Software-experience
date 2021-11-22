volatile unsigned int New_T1, Old_T1, PPS_period ;  // unsigned int: data type which only stores positive intergers 
                                                    // volatile: 'variable qualifer' which directs compiler to load variable from RAM and not from storage register.
 unsigned int pin = 8;                             // assign pin for external intterupt
 bool flag = LOW;
 byte prescalar = B01000010;
 
// timer 1 capture ISR

ISR(TIMER1_CAPT_vect)                    // Interrupt service routines complete outlined task(s) whenever an interrupt is detected
{
    New_T1 = ICR1 ;                    // read timer1 and input to capture register
    flag = HIGH;
}

void setup()
{
  Serial.begin(9600);          // Setting data rate to 9600 bits per second
  
  //TCCR1B &=~ (1<<ICES1) + 1 | (1<<CS12) | (1<<CS10) | (1<<CS11) ;    // 7 bit register, sets first bit corresponding to the ICES1 to 1 for rising edge.
  TCCR1B = prescalar;
  //TCCR1B = (1<<ICES1) +1  | (1<<CS12) | (1>>CS10);         // Bits 0,1,2 corresponding to CS12, CS11, CS10 (Clock select bit)must be changed to determine prescalar.
  TIMSK1 = (1<<ICIE1) ;      
  TCCR1A = 0;                                                  // Register was set to 68 as this is the only combination (ask about method name)) corresponding to prescalar of 256 as referenced by table of register setting bits
              
}


void loop()
{
  if (flag){
    PPS_period =  New_T1 - Old_T1;    // compute time between consecutive measurements in capture register
    Old_T1 = New_T1 ;                // reset measurement to compare duration between next pulse
   
    flag = LOW;
    
    Serial.println( PPS_period);   // Print period between rising edges to check if programme is working
  }
//  delay(990);
}


// timer behaviour is changed using timer registers, such as;

//TCCR1B - timer/counter control register for timer 1, register used to set pre-scalar (divide CPU frequency by a desired factor)
//ICES1 - input capture edge select for timer 1, =1 for trigger on rising edge and =0 for trigger on falling edge.

// '<<' is the left shift operator which causes bits on the left operand to be shifted left by the number of positions specificed by the right operand
//Corresponds to left operand multiplied by 2 raised to the power of the right operand, e.g. 5<<3 = 40
//Set timer1 to capture to rising edge.

//TIMSK1 - Timer/counter interrupt mask register, register used to enable/disable timer intterupts
//ICIE1 - input capture interrupt edge for timer 1
// Enable timer intterupts when the condition is met, 1 is musch less than the interrupt edge

//TCCR1A - timer/counter control register for timer 1
//disable other timer1 functions
// find method to input data into an array on matlab, let programme run for a long period and plot allen deviation of test clock (arduino's oscillator) against reference (gps module pps)
