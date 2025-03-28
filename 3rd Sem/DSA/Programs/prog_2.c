#include <stdio.h>

int main() {
    int num;
    long long factorial = 1; // Initialize factorial to 1

    // Input from the user
    printf("\nEnter a positive integer: ");
    scanf("%d", &num);

    // Check if the input is negative
    if (num < 0) {
        printf("Factorial is not defined for negative numbers.\n");
    } else {
        // Calculate factorial
        for (int i = 1; i <= num; i++) {
            factorial *= i;
        }

        // Output the factorial
        printf("\nFactorial of %d = %lld\n\n", num, factorial);
    }

    return 0;
}
