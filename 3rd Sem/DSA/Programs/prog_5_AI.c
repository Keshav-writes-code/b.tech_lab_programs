#include <stdio.h>
#include <stdlib.h>

void push(int i, int *a, int **t, int **m){
    if (*m == *t){
        printf("Overflow\n");
        return;
    }
    printf("Pushed %d\n", i);
    **t = i;
    (*t)++;
}

int pop(int *a, int **t, int **n){
    if (*t == *n || *t < *n){
        return -1;
    }else{
        (*t)--;
        return **t;
    }
}

void display(int *a, int *t){
    if (t == &a[0]){
        printf("No Elements\n");
        return;
    }
    for (int *i = &a[0]; i < t; i++){
        printf("%d", *i);
        if (!(i == t - 1))
        {
            printf(", ");
        }
    }
    printf("\n");
}

int main(){
    printf("--- Stack in C ---\n");

    int *a;
    int s;
    printf("Initial Size: ");
    scanf("%d", &s);
    a = (int *)malloc(sizeof(int) * s);

    int *m = &a[s];
    int *t = &a[0];
    int *n = &a[0];

    char c;
    do{
        int o;
        printf("\n--- Menu ---\n");
        printf("1. Push\n2. Pop \n3. Change Size\n4. Exit\nOption: ");
        scanf("%d", &o);

        switch (o){
        case 1:
            printf("\nSTACK Before:\n");
            display(a, t);
            printf("\nPush Item: ");
            int i;
            scanf("%d", &i);
            push(i, a, &t, &m);
            printf("\nSTACK After:\n");
            display(a, t);
            break;

        case 2:{
            printf("\nSTACK Before:\n");
            display(a, t);
            printf("\nPopping:\n");
            int r = pop(a, &t, &n);
            if (r == -1){
                printf("Underflow\n");
            }else{
                printf("Popped %d\n", r);
            }
            printf("\nSTACK After:\n");
            display(a, t);
            break;
        }

        case 3:
            printf("New Size: ");
            int ns;
            scanf("%d", &ns);
            if (ns >= t - &a[0]){
                a = (int *)realloc(a, sizeof(int) * ns);
                m = &a[ns];
                printf("size changed successfully.\n");
            }else{
                printf("Error: Cannot reduce stack size below the current number of elements.\n");
            }
            break;

        case 4:
            printf("Exiting\n");
            free(a);
            exit(0);

        default:
            printf("Invalid Option!\n");
            break;
        }

        printf("\nAgain? (Y/N): ");
        scanf(" %c", &c);
    } while (c == 'Y' || c == 'y');
}