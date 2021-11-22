#include <stdio.h>

void main()
{
	float x, y, result;
	
	printf("Enter a value for x: ");
	scanf("%f", &x);
	printf("Enter a value for y: ");
	scanf("%f", &y);
	result = x + y;
	
	  {
		  printf("x + y = %.2e\n", result);
	  }
}