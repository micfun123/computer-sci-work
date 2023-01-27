#include <stdio.h>
#include <stdlib.h>

#define MAX 10
int stack[MAX];
int top = -1;
int choice, item;

void insert(int item)
{
    if (top == MAX - 1)
        printf("Queue overflow \n");
    else
    {
        top = top + 1;
        stack[top] = item;
    }
}

void peek()
{
    if (top == -1)
        printf("Queue is empty \n");
    else
    {
        printf("Queue is : \n");
        for (int i = top; i >= 0; i--)
            printf("%d \n", stack[i]);
    }
}

void pop()
{
    item = stack[top];
    top = top - 1;
    printf("Element deleted from stack is : %d \n", item);
}

void main()
{

    while (1)
    {
        printf("\n\nPress 1 to insert an element into the stack \n Press 2 to delete an element from the stack \n Press 3 to display the stack \n Press 4 to exit \n");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            printf("\nEnter the element to be inserted \n");
            scanf("%d", &item);
            insert(item);
            break;
        case 2:
            pop();
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