#include <stdio.h>
#include <math.h>

double x;

double F(double y)
{
  return x + y;
}

main()
{
  x = 10.;

  printf("the value of x + 2 = %e\n", F(2.));
}
