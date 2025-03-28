#include <stdio.h>

int main() {
    int num, isPrime = 1;

    // Input
    printf("\nEnter a positive integer: ");
    scanf("%d", &num);

    // Check if the number is prime
    if (num <= 1) {
        isPrime = 0; // 0 and 1 are not prime numbers
    } else {
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                isPrime = 0; // Not prime if it has a divisor other than 1 and itself
                break;
            }
        }
    }

    // Output
    if (isPrime) {
        printf("\n%d is a prime number.\n\n", num);
    } else {
        printf("\n%d is not a prime number.\n\n", num);
    }

    return 0;
}
