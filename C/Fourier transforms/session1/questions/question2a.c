#include <stdio.h>

 void main() {
 int N,n,t,s ;

 printf("value of variable N: ");
 scanf("%d", &N);

n = 1;
s = 0;
t = 0;

 do {
  n = s*s;
  t = t + n;
  s = s + 1; }
   while (s <= N);
   
   printf("The summation of N is %d\n",t);
}
