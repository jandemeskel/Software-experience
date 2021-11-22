#include <stdio.h> 
#include <math.h>
#define PI 3.14159265
 
double Re(double t) 
{
return cos(t);
}

double Im(double t)
{
return sin(t);
}

main()
{
double t = (3.14159265/2);
printf(" h1 = %1.1lf + %1.1lf i \n", Re(t), Im(t));

