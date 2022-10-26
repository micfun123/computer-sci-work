#include <stdio.h>

void main(){
    int a = 0;
    int b = 0;
    int z = 0;
    int total = 0;
    int amount = 0;

    printf("What should be the starting number: ");
    scanf("%d",&b);
    printf("How many places should we go up: ");
    scanf("%d",&amount);

    for (int i = 0; i < amount; i++)
    {
        z = a + b;
        total = total + z;
        printf("%d ",z);
        a = b;
        b = z;
    }
    printf("\n your total is %d ",total);
}