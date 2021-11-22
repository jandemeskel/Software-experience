#include <stdio.h>

int main ()
 {
   double x; double *p_x;

   p_x = &x; // set p_x equal to address of x
   *p_x = 10.; // at address given by p_x, store double 10.0
    printf("x = %e\n", x); 
    printf("p_x, the pointer to x, is %p\n", p_x); 
    printf("address of x in memory = %p\n", &x); 
    printf("address of p_x in memory = %p\n", &p_x);
    return 0;
}
