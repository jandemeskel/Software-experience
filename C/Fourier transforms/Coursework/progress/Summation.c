#include <stdio.h> 
#include <math.h>
#define PI 3.14159265

 float main()
{
	FILE *h1, *h2, *h3, *h1_prime, *h2_prime, *h3_prime; 
	float t, n, k, j, i, t_k;
	float h3Re[200], h3Im[200];
	int H3_amp[] = {1,3,4,13};
	
	h3 = fopen("h3.txt", "r");
	for (int i = 0; i < 200; i++)
	{
		fscanf(h3, "%d, %e, %e, %e", &i, &t_k, &h3Re[i], &h3Im[i]);   
	}
	fclose(h3);
	
	h3_prime = fopen("h3_prime.txt","w");
    for (int j=0 ; j<200; j++) 
	{
		
		float sum_h3_primeRe = 0;
	    float sum_h3_primeIm = 0;
		
	    for (n = 1; n < 200; n++)
		{
			if ( n == H3_amp[0] || n == H3_amp[1] || n == H3_amp[2] || n == H3_amp[3] )
			{	
			float sum_H3Re = 0;
	        float sum_H3Im = 0;
			
			for (int k = 0; k < 200; k ++)
			{				
				float cpx_arrayH3[] = {h3Re[k]*cos(PI*n*k/100) + h3Im[k]*sin(PI*n*k/100), h3Im[k]*cos(PI*n*k/100) - h3Re[k]*sin(PI*n*k/100)};
			
				sum_H3Re = sum_H3Re + cpx_arrayH3[0];
				sum_H3Im = sum_H3Im + cpx_arrayH3[1];			
			
			}
			float cpx_arrayh3prime[] = {cos(PI*n*j/100)*sum_H3Re - sin(PI*n*j/100)*sum_H3Im, sin(PI*n*j/100)*sum_H3Re + cos(PI*n*j/100)*sum_H3Im};
			
			sum_h3_primeRe = sum_h3_primeRe + cpx_arrayh3prime[0];
			sum_h3_primeIm = sum_h3_primeIm + cpx_arrayh3prime[1];	
		
		}
		fprintf(h3_prime, " h3_prime = %1.2f + i(%1.2f)  \r\n", sum_h3_primeRe/200, sum_h3_primeIm/200);
		}
		return 0;
	}
	fclose(h3_prime);					
}