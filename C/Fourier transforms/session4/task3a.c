#include <stdio.h>

int main()
{
  char my_string[] = "Hello this is a string.";
  int i = 0;
  
  printf("my_string points at %p\n", my_string);

  do
  {
    printf("at address %p, character %c, stored as %hd\n",
      &my_string[i], my_string[i], my_string[i]);
    i++;
  }
  while (my_string[i] != '\0');
  
  return 0;
}

