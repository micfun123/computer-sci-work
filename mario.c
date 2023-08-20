#include <stdio.h>


int main(void)
{
    int height; //get user input
    do
    {
        printf("Height: ");
        scanf("%d", &height);
    }
    while (height < 1 || height > 8);

    for (int line = 0; line < height; line++)
    {

        for (int space = height - 1; space > line; space = space - 1)   //prints spaces
        {
            printf(" ");
        }

        for (int hash = - 1; hash < line; hash++)   //prints hashes
        {

            printf("#");
        }
        printf(" ");
        for (int hash = -1; hash < line; hash++)
        {
            printf("#");
        }


        printf("\n"); //new line
    }
}