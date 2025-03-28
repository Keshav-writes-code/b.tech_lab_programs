#include <stdio.h>

int main() {
    int value;

    printf("Enter an integer: ");

    // Attempt to read an integer
    if (scanf("%d", &value) == 1) {
        printf("You entered an integer: %d\n", value);

        // Further implementation with the entered integer value
        int result = value * 2;
        printf("Result of further implementation: %d\n", result);
    } else {
        // Check if the failure was due to an empty input
        int c = getchar();
        if (c == '\n') {
            printf("You entered an empty value.\n");
        } else {
            printf("You did not enter a valid integer.\n");
        }
    }

    return 0;
}

