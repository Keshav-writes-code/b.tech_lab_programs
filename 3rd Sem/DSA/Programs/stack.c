#include<stdio.h>

int main(){
    int n= 19;
    int arr[n];
    int top = -1;

    // push
    top++;
    arr[top] = 32;
    
    // push
    top++;
    arr[top] = 43;

    // pop
    top--;
    
    // Peek
    printf("%d\n", arr[top]);


    
}