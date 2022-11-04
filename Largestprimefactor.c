//The prime factors of 13195 are 5, 7, 13 and 29. target 600851475143

#include <stdio.h>

void main(){
    long long number = 0;
    long long largest = 0;
    long long i = 0;
    printf("Enter num \n");
    scanf("%ld",&number);

    for (long long i = 2; i < number; i++)
    {
        printf("%ld\n",i);
        if (number % i == 0)
        {
           largest = i;
           number = number / i;
        }
        

    }
    printf("%ld",largest);
}
