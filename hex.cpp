#include <stdio.h>
#include <stdlib.h>
#include <math.h>



void to_hex(int num){
    int hex[100];
    int i = 0;
    while (num != 0)
    {
        hex[i] = num % 16;
        num = num / 16;
        i++;
    }
    for (int j = i - 1; j >= 0; j--)
    {
        if (hex[j] > 9)
        {
            printf("%c", hex[j] + 55);
        }else
        {
            printf("%d", hex[j]);
        }
    }
    
}


int main(){
    int num = 0;
    printf("Enter a number: ");
    scanf("%d", &num);
    to_hex(num);
    return 0;
}