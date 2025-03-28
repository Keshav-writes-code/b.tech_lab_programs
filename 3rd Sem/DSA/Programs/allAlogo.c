#include <stdio.h>

void display(int* arr, int arrLen) {
    for (int i = 0; i < arrLen; i++) {
        printf("%d%s", arr[i], (i == arrLen - 1) ? "\n" : ", ");
    }
}

void isrtSort(int* arr, int arrLen) {
    for (int i = 1; i < arrLen; i++) {
        int key = arr[i], j = i - 1;
        while (j >= 0 && key < arr[j]) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
    printf("Sorting Using\nInsertion Sort:-\n");
    display(arr, arrLen);
}

void selSort(int* arr, int arrLen) {
    for (int i = 0; i < arrLen - 1; i++) {
        int smallest = i;
        for (int j = i + 1; j < arrLen; j++) {
            if (arr[j] < arr[smallest]) {
                smallest = j;
            }
        }
        int temp = arr[smallest];
        arr[smallest] = arr[i];
        arr[i] = temp;
    }
    printf("Sorting Using\nSelection Sort:-\n");
    display(arr, arrLen);
}

void bublSort(int* arr, int arrLen) {
    for (int i = 0; i < arrLen; i++) {
        for (int j = 0; j < arrLen - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
    printf("Sorting Using\nBubble Sort:-\n");
    display(arr, arrLen);
}

int main() {
    int arr[] = {42, 15, 7, 89, 23, 56, 11, 31, 66, 5, 72, 3, 98, 27, 19, 61, 13, 84, 39, 2};
    int arrLen = sizeof(arr) / sizeof(arr[0]);
    printf("Random Array: ");
    display(arr, arrLen);

    int input;
    printf("1 - Insertion Sort\n2 - Selection Sort\n3 - Bubble Sort\n\nChoose a Sorting Algo: ");
    scanf("%d", &input);

    switch (input) {
        case 1:
            isrtSort(arr, arrLen);
            break;
        case 2:
            selSort(arr, arrLen);
            break;
        case 3:
            bublSort(arr, arrLen);
            break;
        default:
            printf("Invalid Input\n");
    }
    printf("\n");
    return 0;
}
