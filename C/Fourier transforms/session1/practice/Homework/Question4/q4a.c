#include <stdio.h> 
void main()
{
	FILE *fp;
	int i, j;
	
	fp = fopen("times.txt", "w");   /*Open a file created to be written in */
	
	for (i = 1; i <= 10; i++)
	{
		fprintf(fp, "%d times table:\n", i);
		for (j = 1; j <= 12; j++)
		{
			fprintf(fp, "(%2d x %2d =%3d), \n", i, j, i * j);
		}
		fprintf(fp, "\n");
	}
	fclose(fp);
}
	
