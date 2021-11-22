#include <stdio.h>

void main()
{
	int i, j, result;
	
		printf("Enter a value for variable i: ");   /*keyboard input for variable i*/
		scanf("%d", &i);
		
		printf("Enter a value for variable j: ");   /*keyboard input for variable j*/
		scanf("%d", &j);
		
		result = i/j;                               /*function of programme*/
		{
			printf("i/j = %.3f\n", (float) result);      /*print out result of function*/
		}
}
		

	