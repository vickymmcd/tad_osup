/********** Config *********/
#define MAX_BITS 100                 // max number of bits 
#define WEIGAND_WAIT_TIME  3000      // time to wait for another weigand pulse.  
 
#define DATA0 2 // D6 Green
#define DATA1 3 // D7 White


void setup_prox();
unsigned long read_prox();
