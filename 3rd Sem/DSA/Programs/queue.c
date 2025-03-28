#include <stdio.h>

void insert(int item, int *arr, int n, int *rear)
{
    *rear = *rear +1;
    arr[*rear] = item;
}

int main()
{
    int n = 5;
    int a[n];
    int front = 0;
    int rear = -1;

    int rand[] = {453, 66, 34, 87, 34, 98, 56, 43, 65, 65, 65, 76, 3378, 94};

    for (int i = 0; i < 5; i++)
    {
        insert(rand[i], &a, n, &rear);
    }

    for (int i = 0; i < 5; i++)
    {
        front++;
    }

    // peek
    printf("%d", a[front]);
}