#include <stdio.h>
 
int main () 
{
   int H3_amp[] = {1,3,4,13};

    for (int n = 1; n < 200; n++)
	{
		if( n == H3_amp[0] || n == H3_amp[1] || n == H3_amp[2] || n == H3_amp[3] ) 
		{
			printf("%d \n",n);
		}
   } 
   return 0;
}