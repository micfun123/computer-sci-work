#include <stdio.h>

int main(){
    int a = 0;
    int b;
    int z;
    int total;
    int amount;

    printf("What should be the starting number: ");
    scanf("%d",&b);
    printf("How far should we go up: ");
    scanf("%d",&amount);

    for (int i = 0; i < amount; i++)
    {
        z = a + b;
        printf("%d ",z);
        a = b;
        b = z;
    }
    
}