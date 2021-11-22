#include <stdio.h>

 void main() {
 float x,y;

 printf("value of variable x: ");
 scanf("%f", &x);

 printf("Number to be saved y: ");
 scanf("%f",&y);

 x = x + y;
 printf("x + y is %.2e\n",x);
}

