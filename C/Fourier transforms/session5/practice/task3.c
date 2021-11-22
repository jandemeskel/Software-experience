#include <stdio.h>
#include <math.h>

double F(double x)
{
  return log(x) - 3./2. + 1./2. * sin(x / 2.);
}

double find_zero(char filename, double x0, double x1)

{
  double x_mid = 0.5 * (x1 - x0) + x0;
  int i;

  double f0, f_mid, f1;
  
  FILE *p_file;
  p_file = fopen(filename, "w");
  
  f0 = F(x0);
  f1 = F(x1);

  for (i = 0; i < 100; i++)
  {
    f_mid = F(x_mid);
    if (f0 * f_mid < 0)
    {
     f1 = f_mid;
     x1 = x_mid;
    }
    else
    {
     f0 = f_mid;
     x0 = x_mid;
    }
   x_mid = 0.5 * (x1 - x0) + x0;
   }
   return x_mid;
   fprintf(p_file, "%e, %e\n", x, F(x));
    }
    fclose(p_file);

  int main()
  {
    printf("find zero outcome: %e\n", find_zero(1., 10.));
    return 0;
  }
