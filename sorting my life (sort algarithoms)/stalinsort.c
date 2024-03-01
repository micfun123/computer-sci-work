#include <stdio.h>
#include <stdlib.h>

void stalinSort(int *arr, int *n) {
    int *newArr = (int *)malloc(*n * sizeof(int));
    int j = 0;
    for (int i = 0; i < *n; i++) {
        if (i == 0) {
            newArr[j] = arr[i];
            j++;
        } else if (arr[i] >= newArr[j - 1]) {
            newArr[j] = arr[i];
            j++;
        }
    }
    *n = j;
    for (int i = 0; i < j; i++) {
        arr[i] = newArr[i];
    }
    free(newArr);
}

int main() {
    int arr[] = {1, 7 , 3, 5, 2, 4, 6, 44, 22, 11, 33, 55, 77, 99, 88, 66, 0};
    int n = sizeof(arr) / sizeof(arr[0]);
    stalinSort(arr, &n);
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    return 0;
    free(arr);
    
}
