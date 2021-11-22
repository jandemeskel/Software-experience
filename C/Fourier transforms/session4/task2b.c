#include <stdio.h>

int main()
{
  printf("size of interger is %zu\n", sizeof(int));
  printf("size of character is %zu\n", sizeof(char));
  printf("size of float is %zu\n", sizeof(float));
  printf("size of double is %zu\n", sizeof(double));
  printf("size of long is %zu\n", sizeof(long));
 
  char *p_x;
  int *p_y;
  char my_array[9] = {3,3,3,3,3,3,3,3,3};

  p_x = my_array;
  p_y = my_array;
 
  printf("first location in memeory, according to p_x: %p\n", p_x);
  printf("first location in memory, according to p_y: %p\n", p_y);

 return 0;
}


