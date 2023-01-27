#include <stdio.h>
#include <stdlib.h>

int number_of_disks = 10;
char start = 'A';
char end = 'C';
char temp = 'B';

void tower_of_hanoi(int number_of_disks, char start, char end, char temp)
{
    if (number_of_disks == 1)
    {
        printf("Move disk %d from %c to %c \n", number_of_disks, start, end);
        return;
    }
    tower_of_hanoi(number_of_disks - 1, start, temp, end);
    printf("Move disk %d from %c to %c \n", number_of_disks, start, end);
    tower_of_hanoi(number_of_disks - 1, temp, end, start);
}

void main(){
    tower_of_hanoi(number_of_disks, start, end, temp);
}
