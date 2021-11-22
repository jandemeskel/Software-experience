#include <stdio.h> 
#include <math.h>

/*  file read properly check
void main()
{
  FILE *h3; 
  float k3, t_k, h3Re, h3Im; 
  int i;

  h3 = fopen("h3.txt", "r");
  for (i = 0; i < 200; i++)
  {
    fscanf(h3, "%f, %e, %e, %e", &k3, &t_k, &h3Re, &h3Im);  
    printf(" for k = %d  and h3(t = %e) = %e + i (%e) \n", (int)k3, t_k, h3Re, h3Im);
  }
  fclose(h3);
}

*/


void main()
{
  FILE *h3; 
  float i, t_k, h3Re, h3Im; 
  

  h3 = fopen("h3.txt", "r");
  for (i = 0; i < 200; i++)
  {
    fscanf(h3, "%f, %e, %e, %e", &i, &t_k, &h3Re, &h3Im);  
    printf("%e\n", h3Im);
  }
  fclose(h3);
}




/*
double t_k[200];
double h3Re[200];
double h3Im[200];

int read3()
{
	int k;
	FILE *h3;
	
	h3 = fopen("h3.txt,""r");
	for (int i = 0; i <6; i++)
	{
		fscanf(h3,"%d, %e, %e, %e \n", k, t_k[i], h3Re[i], h3Im[i]);
		printf("h3(t = %e) = %e + i %e \n", t_k[i], h3Re[i], h3Im[i]);
	}
	fclose(h3);
}
*/



