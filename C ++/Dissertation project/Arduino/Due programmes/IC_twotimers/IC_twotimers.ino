
//---------------------------

void TC7_Handler() 
{ 
 const bool inputcaptureA2=TC_GetStatus(TC2, 1) & TC_SR_LDRAS;          
 const bool inputcaptureB2=TC_GetStatus(TC2, 1) & TC_SR_LDRBS;       

 Serial.print("TC7 interrupt! counter value=");                  
 Serial.println(TC_ReadCV(TC2,1));
}

void TC6_Handler() 
{             
 const bool inputcaptureA=TC_GetStatus(TC2, 0) & TC_SR_LDRAS;          
 const bool inputcaptureB=TC_GetStatus(TC2, 0) & TC_SR_LDRBS;    

 Serial.print("TC6 interrupt! counter value = ");                  
 Serial.println(TC_ReadCV(TC2,0));
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
 startTimer6(TC2, 0, TC6_IRQn);                          
 Serial.println("setup complete");
}

//-------------------------------
/* Repeat instructions after ISR*/
//-------------------------------

void loop()
{
 Serial.print("Counter7 value is ");
 Serial.println( TC_ReadCV(TC2,1)); 
 Serial.print("Counter6 value is ");          
 Serial.println( TC_ReadCV(TC2,0));
 delay(4000);
}
