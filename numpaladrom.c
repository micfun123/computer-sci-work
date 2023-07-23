#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool isPalindrome(int x){
    int temp = x;
    int rev = 0;
    while (temp > 0){
        rev = rev * 10 + temp % 10; // 0 * 10 + 1 = 1
        temp /= 10; // 12 / 10 = 1
    }
    return rev == x;

}

int main(){
    int x = 122;
    printf("%d", isPalindrome(x));
    return 0;
}
