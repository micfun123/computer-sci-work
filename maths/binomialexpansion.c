#include <stdio.h>
#include <math.h>

long long int binomialCoefficient(int n, int k) {
    if (k == 0 || k == n)
        return 1;
    else
        return binomialCoefficient(n - 1, k - 1) + binomialCoefficient(n - 1, k);
}

void binomialExpansion(int base_a, int base_b, int power) {
    for (int k = 0; k <= power; k++) {
        int coefficient = binomialCoefficient(power, k);
        double term_a = pow(base_a, power - k);
        double term_b = pow(base_b, k);
        double term = coefficient * term_a * term_b;
        printf("%.2f * x^%d * y^%d + ", term, power - k, k);
    }
}

int main() {
    int base_x = -2;
    int base_y = 1;
    int power = 5;
    binomialExpansion(base_x, base_y, power);
    
    return 0;
}
