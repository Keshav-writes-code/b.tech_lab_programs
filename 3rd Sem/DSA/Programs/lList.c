#include<stdio.h>
#include<stdlib.h>
struct node {
    int data;
    struct node* link;
};

int main(){
    int size;
    printf("enter size: ");
    scanf("%d", &size);
    printf("\n");
    
    struct node* head = NULL;

    struct node* prevNode = NULL; 
    for (int i = 0; i < size; i++){
        int data;
        printf("%d data :- ", i+1);
        scanf("%d", &data);

        struct node* newNode = (struct node *) malloc(sizeof(struct node));
        newNode->data = data;
        if (!(prevNode == NULL)){ prevNode->link = newNode;}
        else{head = newNode;}
        
        prevNode = newNode;
    }
    printf("\n");
    

    // display the nodes
    printf("Displaying the Data :-\n");
    struct node* cNode = head;

    for (int i = 0; i < size; i++){
        printf("Data :- %d\n", cNode->data);
        printf("Link :- %d\n", cNode->link);
        cNode = cNode->link;
    }
    

    return 0;
}