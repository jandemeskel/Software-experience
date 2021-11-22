#include <stdio.h> 
void main()
{
  int i, j;
  for (i = 1; i <= 12; i++)
  {
    printf("%d times table:\n", i);
    for (j = 1; j <= 12; j++)
    {
      printf("%2d x %2d = %3d\n", i, j, i * j);
    }
    printf("\n");
  }
}