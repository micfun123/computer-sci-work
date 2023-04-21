#include <stdio.h>
#include <math.h>

// p^n + 3600 = m^2
// p is prime , n and m are integers


int is_prime(int n)
{
   int i;
   for (i = 2; i <= sqrt(n); i++)
      if (n % i == 0)
         return 0;
   return 1;
}

int main(void)
{
    for (int p = 2; p < 1000; p++)
    {
        if (is_prime(p))
        {
            for (int n = 1; n < 1000; n++)
            {
                for (int m = 1; m < 1000; m++)
                {
                    if (pow(p, n) + 3600 == pow(m, 2))
                    {
                        printf("%d^%d + 3600 = %d^2", p, n, m);
                    }
                }
            }
        }
    }
}
   
    

