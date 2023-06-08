#include <stdio.h>
#include <stdlib.h>
#include <math.h>
<<<<<<< HEAD
=======
#include <stdbool.h>
>>>>>>> 3011347285476b51c24a3d398add1e96445e4fce

// array to be sorted
int data[] = { 5,2,6,1134,13413,54,1,6,89,23,6,8,34,73,4,327,5,324 };

// bubble sort function
<<<<<<< HEAD
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





=======
void bubble(int *array, int size){
    int i = 0;
    int j = 0;
    int temp = 0;
    bool swapped = true;
    while(swapped){
        swapped = false;
        for (size_t i = 0; i < size-1; i++){
            if (array[i] > array[i+1]){
                temp = array[i];
                array[i] = array[i+1];
                array[i+1] = temp;
                swapped = true;
            }
        }
    }
    for (size_t i = 0; i < size; i++){
        printf("%d ", array[i]);
    }
    
}

void main(){
    bubble(data, sizeof(data)/sizeof(data[0]));
}
>>>>>>> 3011347285476b51c24a3d398add1e96445e4fce
