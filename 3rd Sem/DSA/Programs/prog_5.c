#include <stdio.h>
#include <stdlib.h>

void push(int i, int *arr, int **top, int *max){
    if (max == *top){
        printf("Overflow\n");
        return;
    }
    printf("Pushed %d\n", i);
    **top = i;
    (*top)++;
}

int pop(int *arr, int **top, int *min){
    if (*top == min || *top < min){
        return -1;
    }else{
        (*top)--;
        return **top;
    }
}

void display(int *arr, int *top){
    if (top == &arr[0]){
        printf("No Elements\n");
        return;
    }
    for (int *i = &arr[0]; i < top; i++){
        printf("%d", *i);
        if (!(i == top - 1))
        {
            printf(", ");
        }
    }
    printf("\n");
}

int main(){
    printf("\n--- Stack in C ---\n");

    int *arr;
    int size;
    printf("Initial Size: ");
    scanf("%d", &size);
    arr = (int *)malloc(sizeof(int) * size);

    int *max = &arr[size];
    int *top = &arr[0];
    int *min = &arr[0];

    char choice;
    do{
        int o;
        printf("\n--- Menu ---\n");
        printf("1. Push\n2. Pop \n3. Peek\n4. Show\nOption: ");
        scanf("%d", &o);

        switch (o){
        case 1:
            printf("\nPush Item: ");
            int i;
            scanf("%d", &i);
            push(i, arr, &top, max);
            break;

        case 2:{
            printf("\nPopping:\n");
            int r = pop(arr, &top, min);
            if (r == -1){
                printf("Underflow\n");
            }else{
                printf("Popped %d\n", r);
            }
            break;
        }

        case 3:
            printf("\nPeek: %d\n", *(top-1));
            break;

        case 4:
            printf("\nStack:\n");
            display(arr, top);
            
            break;
        default:
            printf("Invalid Option!\n");
            break;
        }

        printf("\nAgain? (Y/N): ");
        scanf(" %c", &choice);
    } while (choice == 'Y' || choice == 'y');
    free(arr);
    exit(0);
}