
//---------------------------
/*Variable declaration*/
//---------------------------

volatile unsigned int New_C, Old_C, Freq_C;
bool flag;

int bitvalue=2048;
int averagearray[108];
int shiftedarray[108];
bool flag2=HIGH;
double average, sum;
int x = 0;


/*float averagefreq(){
  int sum;
  float average;
  for(int j=0; j<10; j++){
    sum = sum + averagearray[j];
  }
  average = sum/10;
  return average;
  Serial.println(average);
}*/



//---------------------------
/*Interrupt service routine*/
//---------------------------

void TC8_Handler() 

{
 const uint32_t status=TC_GetStatus(TC2, 2);            
 const bool inputcaptureA=status & TC_SR_LDRAS;          
 const bool inputcaptureB=status & TC_SR_LDRBS;  
 if (inputcaptureA)
 { 
  New_C = TC2 -> TC_CHANNEL[2].TC_RA;    
  flag = HIGH;    
 }
}

//------------------------------------
/*Timer, Register & Peripheral setup*/
//------------------------------------

void startTimer8(Tc *tc, uint32_t channel, IRQn_Type irq)
{

 REG_TC2_WPMR=0x54494D00;                            
 REG_PIOD_WPMR=0x50494F00;                           
 REG_PIOD_PDR |= PIO_PDR_P7;                                                                                                          
 REG_PIOD_ABSR |= PIO_ABSR_P7;                     
 pmc_set_writeprotect(false);                       
 pmc_enable_periph_clk(ID_TC8);                    
 TC_Configure(tc, channel,  TC_CMR_TCCLKS_TIMER_CLOCK1 | TC_CMR_LDRA_RISING | TC_CMR_LDRB_FALLING); 
 const uint32_t flags=TC_IER_COVFS  | TC_IER_LDRAS;     
 tc->TC_CHANNEL[channel].TC_IER=flags;
 tc->TC_CHANNEL[channel].TC_IDR=~flags;   
 NVIC_EnableIRQ(irq);                                                                             
 TC_Start(tc,channel);                                 
}

void startExternal(Tc *tc, uint32_t channel, IRQn_Type irq) 
{
 REG_TC2_WPMR=0x54494D00;                            
 REG_PIOD_WPMR=0x50494F00;                           
 REG_PIOD_PDR |= PIO_PDR_P9;                                                                                                          
 REG_PIOD_ABSR |= PIO_ABSR_P9;                     
 pmc_set_writeprotect(false);                       
 pmc_enable_periph_clk(ID_TC8);                    
 TC_Configure(tc, channel,  TC_CMR_TCCLKS_XC2 | TC_CMR_LDRA_RISING | TC_CMR_LDRB_FALLING); 
 const uint32_t flags=TC_IER_COVFS  | TC_IER_LDRAS;     
 tc->TC_CHANNEL[channel].TC_IER=flags;
 tc->TC_CHANNEL[channel].TC_IDR=~flags;   
 NVIC_EnableIRQ(irq);                                                                             
 TC_Start(tc,channel);                                 
}

//---------------------
/* Final setup steps */
//---------------------

void setup()
{
 Serial.begin(9600);
 startTimer8(TC2, 2, TC8_IRQn);
 startExternal(TC2, 2, TC8_IRQn);                       
 Serial.println("setup complete");
 pinMode(DAC0, OUTPUT);
 //pinMode(26,OUTPUT);
 //digitalWrite(26,LOW);
 analogWriteResolution(12);
} 
//-------------------------------
/* Repeat instructions after ISR*/
//-------------------------------

void loop()
{
  if (flag){
  
    Freq_C = New_C - Old_C;
    Serial.print("TC8 ");
    Serial.println(Freq_C);
    Old_C = New_C;
    
   
    for(int i=0; i<108; i++){
        averagearray[i]=averagearray[i+1];
      }
     
     
     averagearray[107] = Freq_C;
       
     sum=0;
    
    for(int j=0; j<108; j++){
      sum = sum + averagearray[j];
    }
    
    average = sum/108;
    
    //Serial.println(average);

    

   /* if (flag2){
  if (Freq_C>10000003){
    bitvalue = bitvalue-10;
    }
  if (Freq_C<9999997){
    bitvalue=bitvalue+10;
    }
  if (Freq_C>10000000){
    bitvalue=bitvalue-1;
    }
  if (Freq_C<10000000){
    bitvalue=bitvalue+1;
    }
  if (bitvalue>4095){
    bitvalue=4095;
    }
  if (bitvalue<0){
    bitvalue=0;
    }
  if (Freq_C==10000000){
    flag2 = LOW;
  }
    }*/
    
  if (x==108){
    /*if (average>10000000){
       bitvalue=bitvalue-1;
    }
  if (average<10000000){
    bitvalue=bitvalue+1;
  }*/
  if (average>10000000){
    bitvalue=bitvalue-abs(average-10000000)*10;
  }
  if (average<10000000){
    bitvalue=bitvalue+abs(average-10000000)*10;
  }
    if (bitvalue>4095){
    bitvalue=4095;
    }
  if (bitvalue<0){
    bitvalue=0;
    }
  
  /*if (average>10000000){
    do{
      bitvalue=bitvalue-1;
    }while(average=!10000000);
    }
  
  if (average<10000000){
    do{
      bitvalue=bitvalue+1
    }while(average=!10000000);
  
  }*/
  x=0;
  }

  x=x+1;
  analogWrite(DAC0, bitvalue);
  //Serial.println(bitvalue);
  flag = LOW;
  
}
}

  
  

/* Serial.print("timer value is ");
 Serial.println( TC_ReadCV(TC2,2));           
 delay(4000); */
