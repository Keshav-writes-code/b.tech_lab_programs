#include<iostream>
using namespace std;

void merge(int arr[],int temp[],int left,int mid,int right){
    int i=left;
    int j=mid+1;
    int k=left;
    while(i<=mid && j<=right){
        if(arr[i]<=arr[j]){
            temp[k++]=arr[i++];
        }
        else{
            temp[k++]=arr[j++];
        }
    }
    while(i<=mid){
        temp[k++]=arr[i++];
    }
    while(j<=right){
        temp[k++]=arr[j++];
    }
    for(int i=left;i<=right;i++){
        arr[i]=temp[i];
    }
}
void mergeSort(int arr[],int temp[],int left,int right){
    if(left<right){
        int mid=(left+right)/2;
        mergeSort(arr,temp,left,mid);
        mergeSort(arr,temp,mid+1,right);
        merge(arr,temp,left,mid,right);
    }
}

int main(){
    // implement merge sort
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    int temp[n];
    mergeSort(arr,temp,0,n-1);
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;

    return 0;
}