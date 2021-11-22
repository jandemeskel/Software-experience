#include <stdio.h> 
void main()
{
	int x, y;
	{
		printf("Enter a value for x: ");
		scanf("%d", &x);
		printf("Enter a value for y: ");
		scanf("%d", &y);
		{
			if(x > y)
				printf("x is greater than y \n");
			else
			{
				if(x < y)
					printf("x is less than y \n");
				else
					printf("x is equal to y \n");
			}
		}
	}
}