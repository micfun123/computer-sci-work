#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// array to be sorted
int array[] = { 5,2,6,1134,13413,54,1,6,89,23,6,8,34,73,4,327,5,324 };

// merge function
void merge(int *array){
    if (sizeof(array) > 1){
        int mid = floor (sizeof(array)/2);
        int left[mid];
        int right[sizeof(array)-mid];

        int i = 0;
        int j = 0;
        int k = 0;

        while (i < sizeof(left) && j < sizeof(right)){
            if (left[i] < right[j]){
                array[k] = left[i];
                i++;
            } else {
                array[k] = right[j];
                j++;
            }
            k++;
        }
        while (i < sizeof(left)){
            array[k] = left[i];
            i++;
            k++;
        }
        while (j < sizeof(right)){
            array[k] = right[j];
            j++;
            k++;
        }
        int x = 0;
        while (x < sizeof(array)){
            printf("%d ", array[x]);
            x++;
        }

    }
}
void main(){
    merge(array);
}