#include <stdio.h>
#include <math.h>

double F(double x)  // declare function of type double float//
{
  return sin(x) - 2. * log(x + 1.) + x * x / 5.0;
}

void write_file(char *filename, double x0, double x1)

{
  int i;
  double x;

  FILE *p_file;

  p_file = fopen(filename, "w");

  for (i = 0; i <= 100; i++)
  { x = x0 + i * (x1-x0) / 100;
  fprintf(p_file, "%e, %e \n", x, F(x));

 }
 fclose(p_file);
}

 int main()
 {
   write_file("data.txt", 0., 5.0);

  return 0;
}


