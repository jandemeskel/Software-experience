#include <stdio.h>

void main()
{
	int i, n;
	int sum = 0;
	
	printf("enter the number: ");
	scanf("%d", &n);
	
	for(i = 1; i<n; i++)
	{
		sum = sum + i;
	}
	printf("summation is %d", sum);
}