#include <stdio.h>

void main()
{
	int N, n, s;   /* N iteration no. , n sum counter, squared sum of terms */
	
	printf("Pick a value for the number of summations (variable N):");     /* Keyboard input upper bound of sum */
	scanf("%d", &N);
	
	s = 0;   /* Starting sum of terms */
	n = 1;   /* lower bound of sum*/
	do
	 {
		 s += n * n;   /* += operator means a = a + b, previous number + addition, in this cause s = s + (n*n) */
		 n++;          /* increase n by one and repeat summation */
	 }
	 while ( n <= N);  /* limiting condition which ends the loop */
	 printf("Summation of n squared between 1 and N is: %d\n", s);
}
	
	