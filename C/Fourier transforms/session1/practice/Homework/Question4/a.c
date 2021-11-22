#include <stdio.h> 

int factorial(int x)
{
  if (x <= 1) 
  {
    return 1; 
  }
  factorial(x - 1));
  return x * factorial(x - 1);  
}
int main()
{
  int result; 
  int input = 4;
  result = factorial(input);
  printf("%d! is equal to %d\n", input, result);
  return 0; // all is well
}
	