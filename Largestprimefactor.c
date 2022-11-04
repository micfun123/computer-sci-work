//The prime factors of 13195 are 5, 7, 13 and 29. target 600851475143

#include <stdio.h>

void main(){
    long long int target;
    long long int i = 2;
    printf("Enter the number you want to find the largest prime factor of\n");
    scanf("%lld", &target);
    while(i < target){
        if(target % i == 0){
            target = target / i;
        }
        else{
            i++;
        }
    }
    printf("%lld", i);
}