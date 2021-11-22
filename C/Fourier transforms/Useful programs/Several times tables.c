#include <stdio.h> 
void main()
{
	int x = 10;    /* declare interger variable x */
	
	while(--x)     /*while x decreases in increments of 1 */
	{
		printf("%f\n",(float)5/x);      /* print the value of 5 divided by each increment of x as a floating number*/
		                                /* i expect the program to stop when x decreases to zero as this point is undefined */
	}
}