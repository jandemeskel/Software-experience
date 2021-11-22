#include <stdio.h>

 void main () {
  FILE *fp;
  float x, y;
 
  printf("Number to be saved: ");
  scanf("%f",&x);
  fp = fopen("data.txt","w");
  fprintf(fp,"%f\n",x);
  fclose(fp);
  fp = fopen("data.txt","r");
  fscanf(fp,"%f",&y);
  printf("Number saved was %f\n",y);
  fclose(fp);
 }

