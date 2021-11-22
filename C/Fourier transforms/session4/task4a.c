#include <stdio.h>
#include <stdlib.h>

int main()
{
 char A[1000];
 char *B;

 B = malloc (100*sizeof(char));
 printf("first memory address allocated %p\n", B);
 free(B); 
 return 0;
}
