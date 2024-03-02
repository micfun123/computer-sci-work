#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int array[], int low, int high) {
    int pivot = array[low];
    int i = low + 1;
    int j = high;

    while (1) {
        while (i <= j && array[i] <= pivot)
            i++;
        while (array[j] >= pivot && j >= i)
            j--;
        if (j < i)
            break;
        swap(&array[i], &array[j]);
    }
    swap(&array[low], &array[j]);
    return j;
}

void quicksort(int array[], int low, int high) {
    if (low < high) {
        int pivot_index = partition(array, low, high);
        quicksort(array, low, pivot_index - 1);
        quicksort(array, pivot_index + 1, high);
    }
}

int main() {
    int datatosort[] = {3, 6, 8, 10, 1, 2, 1, 42, 2, 15, 57};
    int n = sizeof(datatosort) / sizeof(datatosort[0]);
    
    quicksort(datatosort, 0, n - 1);
    
    printf("Sorted array: ");
    for (int i = 0; i < n; i++)
        printf("%d ", datatosort[i]);
    printf("\n");
    
    return 0;
}
