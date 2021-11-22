
//---------------------

volatile unsigned int New_C1, Old_C1, Freq_C1;
void TC6_Handler() 
{             
 const bool inputcaptureA=TC_GetStatus(TC2, 0) & TC_SR_LDRAS;          
 const bool inputcaptureB=TC_GetStatus(TC2, 0) & TC_SR_LDRBS;    

 Serial.println("TC6 interrupt! ");
 Serial.print("New count value is ");
  if(inputcaptureA) 
  {
    New_C1= TC2->TC_CHANNEL[0].TC_RA;
    Serial.println(New_C1);
    Freq_C1 = New_C1 - Old_C1;
    Serial.print("Frequncy count value is ");
    Serial.println(Freq_C1);
    Old_C1 = New_C1;
    Serial.print("Old count value was ");
    Serial.println(Old_C1);
    Serial.println();
 }                
}

//---------------------

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

void setup()
{
 Serial.begin(9600);
 startTimer6(TC2, 0, TC6_IRQn);                          
 Serial.println("setup complete");
}

void loop()
{
  Serial.print("Counter6 value is ");          
  Serial.println( TC_ReadCV(TC2,0));
  delay(4000);
}

/* To Do List
 *  Subtract consecutive timer counter values to find frequency counts per PPS 
 *  Export frequency counts per PPS to Matlab array "freq_array"
 *  Run allen deviation programme
 *  Repeat for two clocks simultaneously
 *  
 *  Place antenna's connected to GPS modules far apart, to recieve two distinct PPS signals, compare stability.
 *  Find signal stability measuring scale for quantative comparsion
 */
