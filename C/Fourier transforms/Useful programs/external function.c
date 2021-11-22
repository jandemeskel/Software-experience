#include <stdio.h> // we want to print
#include <math.h> // we want to use ’pow’

double F(double x) // ’x’ is argument, function returns ’double’
{
	if (x >= 0)
		return x*x + 3. * x + 2.;
	else
		return -10. * pow(x, 4.) + 2.;
}

double main()
{
	double x1, x2;
	x1 = 1.;
	x2 = 0.;
	
	printf("F(%1.1lf) = %1.1lf\n", x1, F(x1));
	printf("F(%1.1lf) = %1.1lf\n", x2, F(x2));
}
