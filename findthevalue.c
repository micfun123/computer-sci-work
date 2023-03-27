#include <stdio.h>
#include <math.h>

int main(void)
{
    int p = 0;
    int m = 0;
    int n = 0;
    int i = 0;
    int j = 0;
    int k = 0;
    printf("p = %d, m = %d, n = %d", p, m, n);
    while (1)
    {
        if (pow(p,n) + 3600 == pow(m,2))
        {
            printf("p = %d, m = %d, n = %d", p, m, n);
            break;
        }
        else
        {
        
            for  (i = 0; i < 600; i++)
            {
                for (j = 0; j < 600; j++)
                {
                    for (k = 0; k < 600; k++)
                    {
                        p = i;
                        m = j;
                        n = k;
                    }
                }
            }
        }
    }
}