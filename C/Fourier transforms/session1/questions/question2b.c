#include <stdio.h>

 void main() {
  int N, n, t;

 printf("value of variable N: ");
 scanf("%d", &N);

 for(n=0;n<=10;n++) {
   t = n * N;
   printf("The N times table is %d\n",t);
 }
}

