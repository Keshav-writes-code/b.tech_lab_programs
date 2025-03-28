#include <stdio.h>
#include <time.h>
void display(int *arr, int length) {
  for (int i; i < length; i++) {
    printf("%d", arr[i]);
    if (!(i == length)) {
      printf(", ");
    }
  }
  printf("\n");
}
void swap(int *a, int *b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

int partition(int *arr, int swp, int length) {
  for (int i = swp + 1; i < length; i++) {
    if (arr[i] < arr[length]) {
      swp++;
      swap(&arr[i], &arr[swp]);
    }
  }
  swp++;
  swap(&arr[length], &arr[swp]);
  return swp;
}

void qSort(int *arr, int low, int high) {
  if (low < high) {
    int pi = partition(arr, low - 1, high);
    qSort(arr, low, pi - 1);
    qSort(arr, pi + 1, high);
  }
}

int main() {
  int length;
  double timeTaken;
  clock_t start_time, end_time;
  int arr[length];

  printf("------Quick Sort-------\n");
  printf("Enter Size : ");
  scanf("%d", &length);
  for (int i = 0; i < length; i++) {
    printf("%d :- ", i + 1);
    scanf("%d", &arr[i]);
  }
  printf("\nOriginal Array:\n");
  display(arr, length);

  // start_time = clock();
  qSort(arr, 0, length - 1);
  // end_time = clock();
  // timeTaken = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;
  printf("\nSorted Array:\n");
  display(arr, length);
  // printf("Time Taken to Sort %d Elements : %f Seconds\n", length, timeTaken);
}
