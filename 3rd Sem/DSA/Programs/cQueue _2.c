#include<stdio.h>

#define n 5
int arr[n];
int front = -1;
int rear = -1;


void enQueue(int item){
    printf("\nEn Queue %d ", item);
    if (front == -1)front = 0;
    rear = (rear + 1 )%n;
    if (rear %n == front) printf("(Overflow)");
    arr[rear] = item;
    printf("\n");

    for (int i = 0; i < n; i++)
    {
        printf("%d | ",arr[i]);
    }
    printf("\n");
}


void deQueue(){
    printf("\nDe Queue %d\n", arr[front]);
    arr[front] = NULL;
    front = (front + 1)% n;
    for (int i = 0; i < n; i++)
    {
        printf("%d | ", arr[i]);
    }
    printf("\n");

}


int main(){
    enQueue(10);
    enQueue(43);
    enQueue(65);
    enQueue(342);
    enQueue(231);
    enQueue(2);
    enQueue(54);
    printf("\n- - - - - - - - - - - -\n");

    deQueue();
    deQueue();
    deQueue();
    deQueue();
    printf("\n- - - - - - - - - - - -\n");
    
    enQueue(342);
    enQueue(231);
    enQueue(2);
    enQueue(54);
}