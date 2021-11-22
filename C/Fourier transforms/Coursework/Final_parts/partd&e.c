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
	FILE *h1, *h2;
	float t, n, k;
	
	h1 = fopen("h1.txt","w");
	
	for (t = (PI/50); t  <= (2*PI + PI/50); t += (PI/50))
	{
		
		float t1 = t;
		float cpx_arrayh1[] = {h1Re(t), h1Im(t)};

		fprintf(h1, " h1(t = %1.2f) = %1.2f + i(%1.2f)  \r\n", t, cpx_arrayh1[0], cpx_arrayh1[1]);
	}
		
	fclose(h1);	
	
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

	h2 = fopen("h2.txt","w");
	for (t = (PI/50); t  < (2*PI + PI/50); t += (PI/50))
	{
		float cpx_array3[] = {h2Re(t), h2Im(t)};
		fprintf(h2, " h2(t = %1.2f) = %1.2f + i(%1.2f)  \r\n", t, cpx_array3[0], cpx_array3[1]);
	}
	fclose(h2);
	
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
}