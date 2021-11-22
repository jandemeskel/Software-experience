#include <stdio.h>
#include <math.h> 

double F(double x)
{
    if (x >= 0)
      return x*x + 3. * x + 2.;
    else
      return -10. * pow(x, 4.) + 2.;
}

main()
{
   double x1 = 1.; double x2 = 0.;
   
   printf("F(%1.1lf) = %1.1lf\n", x1, F(x1));
   printf("F(%1.1lf) = %1.1lf\n", x2, F(x2));
}

 
