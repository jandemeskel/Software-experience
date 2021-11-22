
void TCregisters() 
{
 const uint32_t status=TC_GetStatus(TC1, 2);             /* read the interrupt*/
 
 const bool inputcaptureA=status & TC_SR_LDRAS;          /* LDRA is a capture registers corresponding to ICRx.*/
 const bool inputcaptureB=status & TC_SR_LDRBS;          /* read register B (LDRB) status to trigger register A to load.*/  /*Current value in RA displayed only if register is not loaded since the last trigger or since RB has been loaded. (Otherwise consecutive loads of RA will set timer value to 0).*/

 Serial.println(TC_ReadCV(TC1,2));                       /* display register value in serial monitor */
}

void TC5_Handler()
{
  REG_TC1_WPMR=0x54494D00;
  REG_PIOB_WPMR=0x50494F00; 
  REG_PIOB_PDR |= PIO_PDR_P16;
  REG_PIOB_ABSR |= PIO_ABSR_P16;
  pmc_set_writeprotect(false);
  pmc_enable_periph_clk(ID_TC5); 
  TC_Configure(TC1, 2, TC_CMR_WAVE | TC_CMR_WAVSEL_UP_RC | TC_CMR_TCCLKS_XC2); // Set clock input to wavemode, trigger automatically on rising and use external clock signal// register bits on pg 884 of datasheet

  TC1->TC_CHANNEL[2].TC_IER=TC_IER_CPCS;
  TC1->TC_CHANNEL[2].TC_IDR=~TC_IER_CPCS;
  NVIC_ClearPendingIRQ(TC5_IRQn);
  NVIC_EnableIRQ(TC5_IRQn);
  TC_Start(TC1, 2);  // Start the counter on DAC1 pin
}

void setup()
{
 pinMode(67, INPUT);                                 /* set pin to recieve signal from oscillator */
 Serial.begin(9600);
 Serial.println("setup complete");
}

void loop()
{
 Serial.print("timer value is ");
 Serial.println( TC_ReadCV(TC1,2));          
 delay(1000);
}
