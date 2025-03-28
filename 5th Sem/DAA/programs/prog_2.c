#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

int *genRandomArr(int arrLen)
{
    int *arr = (int *)malloc(arrLen * sizeof(int));
    for (int i = 0; i < arrLen; i++)
    {
        int randVal = rand() % (1000 - 1 + 1) + 1;
        arr[i] = randVal;
    }
    return arr;
}

void display(int *arr, int arrLen)
{
    printf("\n");
    for (int i = 0; i < arrLen - 1; i++)
    {
        printf("%d, ", arr[i]);
    }
    printf("%d", arr[arrLen - 1]);
    printf("\n\n");
}

void merge(int *arr, int low, int mid, int high)
{
    int n1 = mid - low + 1, n2 = high - mid, left[n1], right[n2];
    for (int i = 0; i < n1; i++)
        left[i] = arr[low + i];
    for (int j = 0; j < n2; j++)
        right[j] = arr[mid + 1 + j];
    for (int i = 0, j = 0, k = low; i < n1 || j < n2; arr[k++] = (j >= n2 || (i < n1 && left[i] <= right[j])) ? left[i++] : right[j++])
        ;
}

void mergeSort(int *arr, int low, int high)
{
    if (low < high)
    {
        int pi = floor((high + low) / 2);
        mergeSort(arr, low, pi);
        mergeSort(arr, pi + 1, high);
        merge(arr, low, pi, high);
    }
}

void mSort(int *arr, int arrLen)
{
    mergeSort(arr, 0, arrLen - 1);
}

int main()
{
    printf("\n\n");
    srand(time(NULL));
    int arrLen = rand() % (40 - 5 + 1) + 5;
    int *arr = genRandomArr(arrLen);

    printf("--------Original Array---------");
    display(arr, arrLen);

    printf("----------Merge Sort-----------");
    mSort(arr, arrLen);
    display(arr, arrLen);
}