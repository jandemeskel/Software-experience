#include <stdio.h> 
#include <math.h>
#define PI 3.14159265
 
float h1Re(float t)       
{
	return cos(t) + cos(5*t);
}
float h1Im(float t)       
{
	return sin(t) + sin(5*t);
}
float h2Re(float t)
{
	return exp(pow((t - PI),2)/2);
}
float h2Im(float t)
{
	return 0;
}
	
float main()
{
	FILE *h1, *h2, *h1_prime, *h2_prime;
	float t, n, k, j;
	
	h1 = fopen("h1.txt","w");
	
	for (t = (PI/50); t  <= (2*PI + PI/50); t += (PI/50))
	{
		
		float t1 = t;
		float cpx_arrayh1[] = {h1Re(t), h1Im(t)};

		fprintf(h1, " h1(t = %1.2f) = %1.2f + i(%1.2f)  \r\n", t, cpx_arrayh1[0], cpx_arrayh1[1]);
	}
	fclose(h1);	
	
	
	                          /* discrete fourier transform of h1(t) > H(w) */
							  
	printf( "\n");
	printf( " H1(w) functions  \n");
	printf( "\n");
	
	for (n = 0; n < 100; n++)
		{
			float sum_H1Re = 0;
	        float sum_H1Im = 0;
			
			for (k = 0; k < 100; k ++)
			{
				float t_1 = (k * PI )/ 50;
				float cpx_arrayH1[] = {cos(PI*n*k/50)*h1Re(t_1) + sin(PI*n*k/50)*h1Im(t_1), cos(PI*n*k/50)*h1Im(t_1) - sin(PI*n*k/50)*h1Re(t_1)};
				
				sum_H1Re = sum_H1Re + cpx_arrayH1[0];
				sum_H1Im = sum_H1Im + cpx_arrayH1[1];
			}
			printf( " H1(n = %1.2lf) = %1.2lf + i(%1.2lf)  \n", n, sum_H1Re, sum_H1Im);	
		}
		
		
                              /* inverse fourier transform of H(w) > h1(t) */
							
							
	h1_prime = fopen("h1_prime.txt","w");
    for (float j=0 ; j<100; j++) 
	{
		float sum_h1_primeRe = 0;
	    float sum_h1_primeIm = 0;
		
	    for (n = 2; n < 101; n++)
		{
			float sum_H1Re = 0;
	        float sum_H1Im = 0;
			
			for (k = 0; k < 100; k ++)
			{
				float t_1 = (k * PI )/ 50;
				float cpx_arrayH1[] = {cos(PI*n*k/50)*h1Re(t_1) + sin(PI*n*k/50)*h1Im(t_1), cos(PI*n*k/50)*h1Im(t_1) - sin(PI*n*k/50)*h1Re(t_1)};
			
				sum_H1Re = sum_H1Re + cpx_arrayH1[0];
				sum_H1Im = sum_H1Im + cpx_arrayH1[1];			
			
			}
			float cpx_arrayh1prime[] = {cos(PI*n*j/50)*sum_H1Re - sin(PI*n*j/50)*sum_H1Im, cos(PI*n*j/50)*sum_H1Im + sin(PI*n*j/50)*sum_H1Re};
			
			sum_h1_primeRe = sum_h1_primeRe + cpx_arrayh1prime[0];
			sum_h1_primeIm = sum_h1_primeIm + cpx_arrayh1prime[1];	
		
		}
		fprintf(h1_prime, " h1_prime = %1.2f + i(%1.2f)  \r\n", sum_h1_primeRe/100, sum_h1_primeIm/100);
	}
	fclose(h1_prime);
	
	
	 
                              /* discrete fourier transform of h2(t) > H(w) */

							
	h2 = fopen("h2.txt","w");
	for (t = (PI/50); t  < (2*PI + PI/50); t += (PI/50))
	{
		float cpx_array3[] = {h2Re(t), h2Im(t)};
		fprintf(h2, " h2(t = %1.2f) = %1.2f + i(%1.2f)  \r\n", t, cpx_array3[0], cpx_array3[1]);
	}
	fclose(h2);
	
	printf( "\n");
	printf( " H2(w) functions  \n");
	printf( "\n");
	
	for (n = 0; n < 100; n++)
		{
			float sum_H2Re = 0;
	        float sum_H2Im = 0;
			
			for (k = 0; k < 100; k++)
			{
				float t_1= (k * PI )/ 50;
				float cpx_arrayH2[] = {cos(PI*n*k/50)*h2Re(t_1), - sin(PI*n*k/50)*h2Re(t_1)};
			
				sum_H2Re = sum_H2Re + cpx_arrayH2[0];
				sum_H2Im = sum_H2Im + cpx_arrayH2[1];
			}
			printf( " H2(n = %1.2lf) = %1.2lf + i(%1.2lf)  \n", n, sum_H2Re, sum_H2Im);
		}
		
		
	                      	   /* inverse fourier transform of H(w) > h2(t) */

	h2_prime = fopen("h2_prime.txt","w");
    for (float j=0 ; j<100; j++) 
	{
		float sum_h2_primeRe = 0;
	    float sum_h2_primeIm = 0;
		
	    for (n = 1; n < 101; n++)
		{
			float sum_H2Re = 0;
	        float sum_H2Im = 0;
			
			for (k = 0; k < 100; k ++)
			{
				float t_1 = (k * PI )/ 50;
				float cpx_arrayH2[] = {cos(PI*n*k/50)*h2Re(t_1) , - sin(PI*n*k/50)*h2Re(t_1)};
			
				sum_H2Re = sum_H2Re + cpx_arrayH2[0];
				sum_H2Im = sum_H2Im + cpx_arrayH2[1];			
			
			}
			float cpx_arrayh2prime[] = {cos(PI*n*j/50)*sum_H2Re, sin(PI*n*j/50)*sum_H2Re};
			
			sum_h2_primeRe = sum_h2_primeRe + cpx_arrayh2prime[0];
			sum_h2_primeIm = sum_h2_primeIm + cpx_arrayh2prime[1];	
		
		}
		fprintf(h2_prime, " h2_prime = %1.2f + i(%1.2f)  \r\n", sum_h2_primeRe/100, sum_h2_primeIm/100);
	}
	fclose(h2_prime);						   
							   
}