
//---------------------------
/*Interrupt service routine*/
//---------------------------

void TC6_Handler() 
{
 const uint32_t status=TC_GetStatus(TC2, 0);             /* read the interrupt*/

 
 const bool inputcaptureA=status & TC_SR_LDRAS;          /* LDRA is a capture registers corresponding to ICRx.*/
 const bool inputcaptureB=status & TC_SR_LDRBS;          /* read register B (LDRB) status to trigger register A to load.*/  /*Current value in RA displayed only if register is not loaded since the last trigger or since RB has been loaded. (Otherwise consecutive loads of RA will set timer value to 0).*/

 Serial.print("TC6 interrupt! value=");                  /*print timer counter value at point of interrupt*/
 Serial.println(TC_ReadCV(TC2,0));
}

//------------------------------------
/*Timer, Register & Peripheral setup*/
//------------------------------------

void startTimer(Tc *tc, uint32_t channel, IRQn_Type irq) /* functions depending on the three variables TC, channel, irq */
{

 REG_TC2_WPMR=0x54494D00;                            /*Enable Timer clock 2's write protect to be changed*/

 REG_PIOC_WPMR=0x50494F00;                           /*Enable registers write protect to be changed*/

 REG_PIOC_PDR |= PIO_PDR_P25;                       /*Peripherals are connections between the board and central devices, in this case the connection between the pins and time counter.*/
                                                    /*pin 5 is port C (pio = programmed input output // PIO_PDR_P25 Disables the pio from controlling the pin. (PDR = peripheral disbale register)*/
                                                    
 REG_PIOC_ABSR |= PIO_ABSR_P25;                     /*Programme Input/Output_ABSelecRegister //Sets bit to 1 corresponding to selecting perpherial B - Programmed connection between pin 5 and TC6.*/

 pmc_set_writeprotect(false);                       /*disable writeprotect.*/

 pmc_enable_periph_clk(ID_TC6);                     /*turn on peripheral for TC2 channel 0 (turned off by default)*/

 TC_Configure(tc, channel,  TC_CMR_TCCLKS_TIMER_CLOCK1 | TC_CMR_LDRA_RISING | TC_CMR_LDRB_FALLING); /* Timer configuration via setting specifed bits in timer clock channel mode register */ 
                                                                                                    /* (tc, channel, Set prescalar to 2 | trigger to LDRA on rising edge | trigger to LDRB on falling edge) */
 
 const uint32_t flags=TC_IER_COVFS  | TC_IER_LDRAS;     /* Set flag to go high when interrupt occurs on TI0A6 (timer6 input output line A) */
 tc->TC_CHANNEL[channel].TC_IER=flags;
 tc->TC_CHANNEL[channel].TC_IDR=~flags;   

 NVIC_EnableIRQ(irq);                                  /* Enable interrupt of specific device (z) */                                                   

 TC_Start(tc,channel);                                 /* start timer for (clock x, channel y) */
}

//---------------------
/* Final setup steps */
//---------------------

void setup()
{
 Serial.begin(9600);
 startTimer(TC2, 0, TC6_IRQn);                           /* input variables into function startTimer() */
 Serial.println("setup complete");
}

//-------------------------------
/* Repeat instructions after ISR*/
//-------------------------------

void loop()
{
 Serial.print("timer value is ");
 Serial.println( TC_ReadCV(TC2,0));           /*check counter is still active every 4 seconds*/
 delay(4000);
}

/*Written using pg 863 of http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-11057-32-bit-Cortex-M3-Microcontroller-SAM3X-SAM3A_Datasheet.pdf */
/* https://android.googlesource.com/platform/external/arduino-ide/+/f876b2abdebd02acfa4ba21e607327be4f9668d4/hardware/arduino/sam/system/CMSIS/Device/ATMEL/sam3xa/include/instance/instance_pioc.h - peripherals = connection between board and central devices, in this case the baord to timer counters */
/* post #9 https://forum.arduino.cc/index.php?topic=130423.0 */
