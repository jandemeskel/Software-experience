//---------------------------
/*Variable declaration*/
//---------------------------

volatile unsigned int New_C, Old_C, Freq_C;
bool flag;

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
} 
//-------------------------------
/* Repeat instructions after ISR*/
//-------------------------------

void loop()
{
  if (flag)
  {
    Freq_C = New_C - Old_C;
    Serial.print("TC8 ");
    Serial.println(Freq_C);
    Old_C = New_C;
    flag = LOW;
  }
/* Serial.print("timer value is ");
 Serial.println( TC_ReadCV(TC2,2));           
 delay(4000); */
}
