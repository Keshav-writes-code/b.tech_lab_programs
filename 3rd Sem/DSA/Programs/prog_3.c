#include <stdio.h>
#include <stdbool.h>
#include <math.h>

void display(int arr[], int len) {
    printf("\n");
    for (int i = 0; i < len; i++) {
        printf("%d%s", arr[i], (i == len - 1 ? "\n" : ", "));
    }
}

int binarySearch(int arr[], int len, int item) {
    int low = 0, upp = len;
    while (low <= upp) {
        int mid = floor((low + upp) / 2);
        if (arr[mid] == item)
            return mid;
        if (item < arr[mid])
            upp = mid - 1;
        else
            low = mid + 1;
    }
    return -1;
}

int main() {
    int arr[20] = {2, 3, 5, 7, 11, 13, 15, 19, 23, 27, 31, 39, 42, 56, 61, 66, 72, 84, 89, 98};
    int arrlen = sizeof(arr) / sizeof(arr[0]);
    int item;

    printf("\nThe Items: ");
    display(arr, arrlen);

    printf("\nEnter a Value to Search: ");
    if (scanf("%d", &item) != 1) {
        printf("\nNot a valid Input\n");
    } else {
        int index = binarySearch(arr, arrlen, item);
        if (index != -1) {
            printf("Item was Found at index: %d\n", index+1);
        } else {
            printf("Item was not Found :(\n");
        }
    }

    return 0;
}