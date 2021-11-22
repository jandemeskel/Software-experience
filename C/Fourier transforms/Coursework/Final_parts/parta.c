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
	float t;
	printf("Choose the value t for the functions h1(t) & h2(t) to 7 decimal places: ");
	scanf("%f",&t);
	float t1 = t;
	float cpx_array1[] = {h1Re(t1), h1Im(t1)};
	
	
	float t2 = t*5;
	float cpx_array2[] = {h1Re(t2), h1Im(t2)};
	
	printf(" h1(t) = %1.2f + i(%1.2f)  \n", cpx_array1[0]+cpx_array2[0], cpx_array1[1]+cpx_array2[1]);
	
	float cpx_array3[] = {h2Re(t), h2Im(t)};
	
	printf(" h2(t) = %1.2f + i(%1.2f)  \n", cpx_array3[0], cpx_array3[1]);
}


