#include<iostream>
#include<stdlib.h>
#include<time.h>
using namespace std;

#define MAXValue 100
#define MAXLen 20

void display(int *arr, int length){
    for (int i = 0; i < length; i++){
        cout<<arr[i];
        if (!(i == length-1)){
            cout<<", ";
        }
        
    }
    cout<<endl;
}

void merge(int *arr, int *temp, int left, int mid, int right){
    int i = left;
    int j = mid+1;
    int k = left;
    while (i <= mid && j <= right){
        if (arr[i]<=arr[j]){
            temp[k++] = arr[i++];
        }else{
            temp[k++] = arr[j++];
        }
    }
    while(i <=mid){
        temp[k++] = arr[i++];
    }
    while(j <=right){
        temp[k++] = arr[j++];
    }
    for (int i = left; i <= right; i++){
        arr[i] = temp[i];
    }
}

void mergeSort(int *arr, int *temp, int left, int right){
    if (left<right)
    {
        int mid = (left +right)/2;
        mergeSort(arr, temp, left, mid);
        mergeSort(arr, temp, mid+1, right);
        merge(arr, temp, left, mid, right);
    }
    
}

int main(){
    srand(time(NULL));
    int n = 10+(rand()%MAXLen);

    int *arr = new int[n];
    for (int i = 0; i < n; i++){
        arr[i] = 10+rand()%MAXValue; 
    }
    cout<<"Original Array :-\n";
    display(arr, n);

    int *temp = new int[n];
    mergeSort(arr, temp, 0, n-1);

    cout<<"\nSorted Array :-\n";
    display(arr, n);

}