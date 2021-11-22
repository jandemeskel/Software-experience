
//---------------------------
/*Interrupt service routine*/
//---------------------------

volatile unsigned int New_C8, Old_C8, Freq_C8, New_C0, Old_C0, Freq_C0;
bool flag1, flag2;

void TC8_Handler() 
{
 const uint32_t status=TC_GetStatus(TC2, 2);            
 const bool inputcaptureA1=status & TC_SR_LDRAS;          
 const bool inputcaptureB1=status & TC_SR_LDRBS;   
  if (inputcaptureA1)
 {
  New_C8 = TC2 -> TC_CHANNEL[2].TC_RA;  
  flag1 = HIGH;
 }       
}

void TC0_Handler() 
{
 const uint32_t status=TC_GetStatus(TC0, 0);            
 const bool inputcaptureA=status & TC_SR_LDRAS;          
 const bool inputcaptureB=status & TC_SR_LDRBS; 
  if (inputcaptureA)
 {
  New_C0 = TC0 -> TC_CHANNEL[0].TC_RA; 
  flag2 = HIGH;    
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

void startTimer0(Tc *tc, uint32_t channel, IRQn_Type irq)
{

 REG_TC0_WPMR=0x54494D00;                            
 REG_PIOD_WPMR=0x50494F00;                           
 REG_PIOD_PDR |= PIO_PDR_P25;                                                                                                          
 REG_PIOD_ABSR |= PIO_ABSR_P25;                     
 pmc_set_writeprotect(false);                       
 pmc_enable_periph_clk(ID_TC0);                    
 TC_Configure(tc, channel,  TC_CMR_TCCLKS_TIMER_CLOCK1 | TC_CMR_LDRA_RISING | TC_CMR_LDRB_FALLING); 
 const uint32_t flags=TC_IER_COVFS  | TC_IER_LDRAS;     
 tc->TC_CHANNEL[channel].TC_IER=flags;
 tc->TC_CHANNEL[channel].TC_IDR=~flags;   
 NVIC_EnableIRQ(irq);                                                                             
 TC_Start(tc,channel);                                 
}
void startExternal1(Tc *tc, uint32_t channel, IRQn_Type irq) 
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

void startExternal2(Tc *tc, uint32_t channel, IRQn_Type irq) 
{
 REG_TC2_WPMR=0x54494D00;                            
 REG_PIOB_WPMR=0x50494F00;                           
 REG_PIOB_PDR |= PIO_PDR_P25;                                                                                                          
 REG_PIOB_ABSR |= PIO_ABSR_P25;                     
 pmc_set_writeprotect(false);                       
 pmc_enable_periph_clk(ID_TC0);                    
 TC_Configure(tc, channel,  TC_CMR_TCCLKS_XC0 | TC_CMR_LDRA_RISING | TC_CMR_LDRB_FALLING); 
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
 startTimer0(TC0, 0, TC0_IRQn);
 startExternal1(TC2, 2, TC8_IRQn);
 startExternal2(TC0, 0, TC0_IRQn);                       
 Serial.println("setup complete");
} 
//-------------------------------
/* Repeat instructions after ISR*/
//-------------------------------

void loop()
{
  if (flag1)
  { 
    Freq_C8 = New_C8 - Old_C8;
    Serial.print("TC8 ");
    Serial.println(Freq_C8);
    Old_C8 = New_C8;  
    flag1 = LOW;
  } 
  if (flag2)
  {  
    Freq_C0 = New_C0 - Old_C0;
    Serial.print("TC0 ");
    Serial.println(Freq_C0);
    Old_C0 = New_C0;  
    flag2 = LOW;
  } 
 /*
 Serial.print("timer value is ");
 Serial.println( TC_ReadCV(TC2,2));           
 delay(4000); */
}
