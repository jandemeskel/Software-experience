#include <stdio.h>
#include <math.h>

int main(int argc, char *argv[]) {
  int i;
  printf("number of inputs %d\n",argc);
  for(i=0;i<argc;i++)  {
    printf("input %d is %s\n",i,argv[i]);
  }
  return 2;
}
