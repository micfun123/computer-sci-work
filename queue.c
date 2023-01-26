#include <stdio.h>
#include <stdlib.h>

#define MAX 10
int queue[MAX];
int front = -1, rear = -1;
int choice, item;

void peek()
{
    if (front == -1)
        printf("Queue is empty \n");
    else
    {
        printf("Queue is : \n");
        for (int i = front; i <= rear; i++)
            printf("%d \n", queue[i]);
    }
}

void insert(int item)
{
    if (rear == MAX - 1)
        printf("Queue overflow \n");
    else
    {
        if (front == -1)
            front = 0;
        rear = rear + 1;
        queue[rear] = item;
    }
}

void Dequeue()
{
    if (front == -1 || front > rear)
    {
        printf("Queue underflow \n");
        return;
    }
    else
    {
        printf("Element deleted from queue is : %d \n", queue[front]);
        front = front + 1;
    }
}

void main()
{

    while (1)
    {
        printf("\n\nPress 1 to insert an element into the queue \n Press 2 to delete an element from the queue \n Press 3 to display the queue \n Press 4 to exit \n");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            printf("\nEnter the element to be inserted \n");
            scanf("%d", &item);
            insert(item);
            break;
        case 2:
            Dequeue();
            break;
        case 3:
            peek();
            break;
        case 4:
            exit(0);
            break;
        }
    }
}