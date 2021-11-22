#include <stdio.h>

int main(){
 int m1[2][3] = { {0,1,2}, {3,4,5} };

 int row;
 int col;
 for(row=0;row<2;row++){
  for(col=0;col<3;col++){
  
    int result = m1[row][col];
    printf("%d\n", result);
  }
 }
}
