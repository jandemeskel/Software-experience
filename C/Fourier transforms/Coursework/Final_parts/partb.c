#include <stdio.h> 
#include <math.h>
#define PI 3.14159265
 
float h1Re(float t)       
{
	return cos(t);
}
float h1Im(float t)       
{
	return sin(t);
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
	float t;
	h1 = fopen("h1.txt","w");
	
	for (t = (PI/50); t  <= (2*PI + PI/50); t += (PI/50))
	{
		
		float t1 = t;
		float cpx_array1[] = {h1Re(t1), h1Im(t1)};
		
		float t2 = t*5;
		float cpx_array2[] = {h1Re(t2), h1Im(t2)};
		
		fprintf(h1, " h1(t = %1.2f) = %1.2f + i(%1.2f)  \r\n", t, cpx_array1[0]+cpx_array2[0], cpx_array1[1]+cpx_array2[1]);
	}
	fclose(h1);	
		
	h2 = fopen("h2.txt","w");
	for (t = (PI/50); t  < (2*PI + PI/50); t += (PI/50))
	{
		float cpx_array3[] = {h2Re(t), h2Im(t)};
		fprintf(h2, " h2(t = %1.2f) = %1.2f + i(%1.2f)  \r\n", t, cpx_array3[0], cpx_array3[1]);
	}
	fclose(h2);
}