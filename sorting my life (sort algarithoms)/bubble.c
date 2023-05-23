#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// array to be sorted
int data[] = { 5,2,6,1134,13413,54,1,6,89,23,6,8,34,73,4,327,5,324 };

// bubble sort function
void bubble(int *array){
    int swapped = 0;
    while (swapped == 0){
        int i = 0;
        for (i = 0; i < sizeof(array); i++){
            if (array[i] > array[i+1]){
                int temp = array[i];
                array[i] = array[i+1];
                array[i+1] = temp;
                swapped = 1;
            }
        }
    }
   printf("%d ", array);

}

void main(){
    bubble(data);
}





