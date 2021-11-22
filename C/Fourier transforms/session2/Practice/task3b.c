#include <stdio.h>
#include <math.h>

double x;

double F(double x, double y)

{
  x = x + y;
  return x;
}

main()
{
  double y;

  x = 10.;
  y = F(x, 30.);

  printf("x = %1.2f, y = %1.2f\n", x,y);
}
