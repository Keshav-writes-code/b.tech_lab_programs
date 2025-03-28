#include<stdio.h>
#include<stdlib.h>
#include<time.h>

#define n 5
int arr[n];
int front = -1;
int rear = -1;

void display(){
    int i = front;

    while (i != rear){    
        printf("%d | ",arr[i]);
        i = (i + 1) % n;
    }

    // for (int i = front; i < front + 5; i++){
    //     printf("%d | ",arr[i%n]);        
    // }
    

    printf("\n");
}

void enQueue(int item){
    if ((rear +1 )%n == front){
        printf("Queue Overflow!\n");
        return;
    }
    
    if (front == -1)front = 0;
    printf("En Queue %d\n", item);
    rear = (rear + 1 )%n;
    arr[rear] = item;

    display();
}


void deQueue(){
    if (front == rear && front == -1){printf("Underflow!\n"); return;} 
    printf("De Queue %d\n", arr[front]);
    arr[front] = NULL;
    if (front == rear && front > -1){front = -1; rear = -1;}
    else front = (front + 1)% n;
    display();
}

int main(){
    int max = 89;
    int min = 10;
    srand(time(NULL));

    deQueue();
    deQueue();

    printf("\n- - - - - - - - - - - -\n");

    enQueue(min + rand()%max);
    enQueue(min + rand()%max);
    enQueue(min + rand()%max);
    enQueue(min + rand()%max);
    enQueue(min + rand()%max);
    enQueue(min + rand()%max);
    enQueue(min + rand()%max);
    printf("\n- - - - - - - - - - - -\n");

    deQueue();
    deQueue();
    deQueue();
    deQueue();

    printf("\n- - - - - - - - - - - -\n");

    enQueue(min + rand()%max);
    enQueue(min + rand()%max);
    enQueue(min + rand()%max);
    enQueue(min + rand()%max);
    enQueue(min + rand()%max);
    enQueue(min + rand()%max);
    enQueue(min + rand()%max);
    printf("\n- - - - - - - - - - - -\n");

    deQueue();
    deQueue();
    deQueue();
    deQueue();
    deQueue();
    deQueue();
    deQueue();
    deQueue();
    deQueue();
    deQueue();
    deQueue();
    deQueue();
    deQueue();

    printf("\n- - - - - - - - - - - -\n");

    enQueue(min + rand()%max);
    enQueue(min + rand()%max);
    enQueue(min + rand()%max);
    enQueue(min + rand()%max);
    enQueue(min + rand()%max);
    enQueue(min + rand()%max);
    enQueue(min + rand()%max);

}