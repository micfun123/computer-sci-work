#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// array to be sorted
int data[] = { 5,2,6,1134,13413,54,1,6,89,23,6,8,34,73,4,327,5,324 };

// merge function
void merge(int *array){
    int size = sizeof(array)/sizeof(array[0]);
    int mid = size/2;
    int left[mid];
    int right[size-mid];
    for (size_t i = 0; i < mid; i++){
        left[i] = array[i];
    }
    for (size_t i = mid; i < size; i++){
        right[i] = array[i];
    }
    merge(left);
    merge(right);
    int i = 0;
    int j = 0;
    int k = 0;
    while(i < mid && j < size-mid){
        if (left[i] < right[j]){
            array[k] = left[i];
            i++;
        }else{
            array[k] = right[j];
            j++;
        }
        k++;
    }
    while(i < mid){
        array[k] = left[i];
        i++;
        k++;
    }
    while(j < size-mid){
        array[k] = right[j];
        j++;
        k++;
    }
    for (size_t i = 0; i < size; i++){
        printf("%d ", array[i]);
    }
}
void main(){
    merge(data);
}