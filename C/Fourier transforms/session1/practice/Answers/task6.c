#include <stdio.h>
void main() {
  int i, j, k;

  i = 0;
  while (i<=10) {
   for (j=0;j<i;j++) {
    if (2*j==i) {
     k =i - j;           //k should equal j
     printf("i = %d is twice j = k = %d\n",i,k);
    }
   }
   i=i+2;
  }
}

