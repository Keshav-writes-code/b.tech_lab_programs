#include <stdio.h>
int MatrixChainOrder(int p[], int n) {
    int m[n][n];
    for (int i = 1; i < n; i++)
        m[i][i] = 0;
    for (int L = 2; L < n; L++) {
        for (int i = 1; i < n - L + 1; i++) {
            int j = i + L - 1;
            m[i][j] = 1000; // Use a large value to simulate infinity
            for (int k = i; k < j; k++) {
                int q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j];
                if (q < m[i][j])
                    m[i][j] = q;
            }
        }
    }
    return m[1][n - 1];
}
int main() {
    int arr[] = {1, 2, 3, 4, 3};
    int size = sizeof(arr) / sizeof(arr[0]);
    printf("Minimum number of multiplications is %d\n", MatrixChainOrder(arr, size));
    return 0;
}
