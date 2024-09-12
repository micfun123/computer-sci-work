#include <stdio.h>

int main()
{
    int arr[2] = {1, 9};
    int i = 0;
    
    arr[i], arr[i+1] = arr[i+1], arr[i];
    
    printf("%d, %d\n", arr[0], arr[1]); // Prints 1, 2
    return 0;
}