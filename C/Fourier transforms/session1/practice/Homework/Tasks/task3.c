#include <stdio.h>
#define PI 3.1415926535
void main() {
int i, j;
double x, y;
/* main program starts here */
i = 3;
j = 8;
j = ++i;
x = PI/2;
y = (float) i/2;
printf("x is %.2f, j is %d, and y = %.2e\n",x,j,y);
}
