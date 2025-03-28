#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void display(int *arr, int *size)
{
    for (int i = 0; i < *size; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
}
void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int Mean(int *arr, int size){
    int sum = 0;
    for (int i = 0; i < size; i++){
        sum += arr[i];
    }
    return sum / size;}

int partition(int *arr, int swp, int l){
    for (int i = swp +1; i < l; i++){
        if (arr[l] > arr[i]){
            swp++;
            swap(&arr[i], &arr[swp]);
        }
    }
    swp++;
    swap(&arr[l], &arr[swp]);
    return swp;
}

void quick(int * arr, int low, int high){
    if (low<high){
        int pi = partition(arr, low-1, high);
        quick(arr, pi+1, high);
        quick(arr, low, pi-1);
    }
}

void quickSort(int * arr, int n){
    quick(arr, 0, n-1);
}

int main()
{
    srand(time(NULL));
    int n = rand() % 20 + 10;
    int arr[n];
    for (int i = 0; i < n-1; i++){
        arr[i] = rand() % 100 + 1;
    }
    arr[n-1] = Mean(arr, n-1);

    printf("Random Array:\n");
    display(arr, &n);

    // Implenting quick sort
    quickSort(arr, n);


    printf("\nSorted Array:\n");
    display(arr, &n);
}