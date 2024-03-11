#include <stdio.h>
#include <stdlib.h>


char start = 'A';
char end = 'C';
char temp = 'B';
long long int count = 0;

void tower_of_hanoi(int number_of_disks, char start, char end, char temp)
{
    count++;
    if (number_of_disks == 1)
    {
        printf("Move disk %d from %c to %c \n", number_of_disks, start, end);
        return;
    }
    tower_of_hanoi(number_of_disks - 1, start, temp, end);
    printf("Move disk %d from %c to %c \n", number_of_disks, start, end);
    tower_of_hanoi(number_of_disks - 1, temp, end, start);
}

//takes the number of disks as input via command line arguments

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: %s <number_of_disks>\n", argv[0]);
        return 1;
    }
    int number_of_disks = atoi(argv[1]);
    tower_of_hanoi(number_of_disks, start, end, temp);
    printf("Total number of moves: %lld\n", count);
    return 0;
}

