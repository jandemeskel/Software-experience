#include <stdio.h> 
void main()
{
	FILE *fp;
	
	fp = fopen("data.txt", "w");   
	fprintf(fp, "9.67\n5.32\n9.98\n2.19\n4.87\n");
	fclose(fp);
}