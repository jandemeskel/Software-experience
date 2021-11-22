#include <stdio.h>

void main()
{
	FILE *fp;
	int x, y;
	
	printf("Saved value of variable x: ");    /*Entering value for variable x from keyboard input*/
	scanf("%d", &x);
	
	fp = fopen("variable values.txt", "w");   /*Open a file created to be written in */
	fprintf(fp,"%d\n",x);
	fclose(fp);
	
	fp = fopen("variable values.txt", "r");  /* reopen file, this time opened to be read*/
	
	fscanf(fp,"%d", &y);                      /* output program saved in file*/
	printf("The value of x saved was: %d\n",y);
	fclose(fp);
	
}
