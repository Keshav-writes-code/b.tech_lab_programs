#include <stdio.h>
#include <stdbool.h>
#include <math.h>

void display(int *arr, int len)
{
    printf("\n");
    for (int i = 0; i < len; i++)
    {
        printf("%d", arr[i]);
        if (!(i == len - 1))
        {
            printf(", ");
        }
    }
    printf("\n");
}

bool binarySrch(int *arr, int len, int item)
{
    int low = 0;
    int upp = len;
    while (low <= upp)
    {
        int mid = floor((low + upp) / 2);
        if (arr[mid] == item)
        {
            return true;
        }
        else if (item < arr[mid])
        {
            upp = mid - 1;
        }
        else
        {
            low = mid + 1;
        }
    }
    return false;
}

int main()
{
    int arr[] = {2, 3, 5, 7, 11, 13, 15, 19, 23, 27, 31, 39, 42, 56, 61, 66, 72, 84, 89, 98};
    int arrlen = sizeof(arr) / sizeof(arr[0]);
    int item;
    printf("\n\nThe Items :-");
    display(arr, arrlen);
    printf("\nEnter a Value to Search :- ");
    if (!(scanf("%d", &item)))
    {
        printf("\n\nNot a valid Input");
        return 0;
    }
    printf("\n");
    printf("%s\n\n", (binarySrch(arr, arrlen, item) ? "Item was Found!" : "Item was not Found :("));
    return 0;
}