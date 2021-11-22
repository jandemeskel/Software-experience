
//---------------------------

volatile unsigned int New_C2, Old_C2, Freq_C2,New_C1, Old_C1, Freq_C1;
bool flag1, flag2;

void TC7_Handler() 
{             
 const bool inputcaptureA2=TC_GetStatus(TC2, 1) & TC_SR_LDRAS;          
 const bool inputcaptureB2=TC_GetStatus(TC2, 1) & TC_SR_LDRBS;    

  if(inputcaptureA2) 
  {
    New_C2= TC2->TC_CHANNEL[1].TC_RA;
    flag1 = HIGH;
 }  
}              

void TC6_Handler() 
{             
 const bool inputcaptureA=TC_GetStatus(TC2, 0) & TC_SR_LDRAS;          
 const bool inputcaptureB=TC_GetStatus(TC2, 0) & TC_SR_LDRBS;    

  if(inputcaptureA) 
  {
    New_C1= TC2->TC_CHANNEL[0].TC_RA;
    flag2 = HIGH;
 }                
} 

//------------------------------------

void startTimer7(Tc *tc, uint32_t channel, IRQn_Type irq) 
{
 REG_TC2_WPMR=0x54494D00;                            
 REG_PIOC_WPMR=0x50494F00;                           
 REG_PIOC_PDR |= PIO_PDR_P28;                                                                                                                             
 REG_PIOC_ABSR |= PIO_ABSR_P28;                     
 pmc_set_writeprotect(false);                      
 pmc_enable_periph_clk(ID_TC7);                     
 TC_Configure(tc, channel,  TC_CMR_TCCLKS_TIMER_CLOCK1 | TC_CMR_LDRA_RISING | TC_CMR_LDRB_FALLING);                                                                                                     
 const uint32_t flags7=TC_IER_COVFS  | TC_IER_LDRAS;     
 tc->TC_CHANNEL[channel].TC_IER=flags7;
 tc->TC_CHANNEL[channel].TC_IDR=~flags7;   
 NVIC_EnableIRQ(irq);                                 
 TC_Start(tc,channel);                                 
} 

void startTimer6(Tc *tc, uint32_t channel, IRQn_Type irq) 
{
 REG_TC2_WPMR=0x54494D00;                            
 REG_PIOC_WPMR=0x50494F00;                           
 REG_PIOC_PDR |= PIO_PDR_P25;                                                                                                                             
 REG_PIOC_ABSR |= PIO_ABSR_P25;                     
 pmc_set_writeprotect(false);                      
 pmc_enable_periph_clk(ID_TC6);                     
 TC_Configure(tc, channel,  TC_CMR_TCCLKS_TIMER_CLOCK1 | TC_CMR_LDRA_RISING | TC_CMR_LDRB_FALLING);                                                                                                     
 const uint32_t flags1=TC_IER_COVFS  | TC_IER_LDRAS;     
 tc->TC_CHANNEL[channel].TC_IER=flags1;
 tc->TC_CHANNEL[channel].TC_IDR=~flags1;   
 NVIC_EnableIRQ(irq);                                 
 TC_Start(tc,channel);                                 
}


//---------------------

void setup()
{
 Serial.begin(9600);
 startTimer7(TC2, 1, TC7_IRQn); 
 delayMicroseconds(20);
 startTimer6(TC2, 0, TC6_IRQn);                          
/* Serial.println("setup complete"); */
}

//-------------------------------
/* Repeat instructions after ISR*/
//-------------------------------

void loop()
{
  if (flag1)
  {
    Freq_C2 = New_C2 - Old_C2;
    Serial.print("TC7 ");
    Serial.println(Freq_C2);  
    Old_C2 = New_C2;
    flag1 = LOW;
  }
  if (flag2)
  {
    Freq_C1 = New_C1 - Old_C1;
    Serial.print("TC6 ");
    Serial.println(Freq_C1);
    Old_C1 = New_C1;
    flag2 = LOW;
  }
 }
 /* Serial.print("timer7 value is ");
 Serial.println( TC_ReadCV(TC2,1)); */          /*check counter is still active every 4 seconds*/
 
/* Serial.print("timer6 value is ");
 Serial.println( TC_ReadCV(TC2,0));           /*check counter is still active every 4 seconds*/
/* delay(4000); */
