def lSrch(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return -1
def bSrch(arr, item):
    low = 0
    high = len(arr) -1
    while low <= high:
        mid = (low + high) //2
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            high = mid-1
        elif arr[mid] < item:
            low = mid +1
    return -1
def selSort(arr):
    for i in range(len(arr)-1):
        minVal = i
        for j in range(i+1, len(arr)-1):
            if arr[minVal] > arr[j]:
                minVal = j
        arr[i], arr[minVal] = arr[minVal], arr[i]
    return arr
def bSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
def iSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a,b = 0,1
        for _ in range(2, n+1):
            a,b = b, a+b
        return b

print("Fibbonci Number : ",fib(int(input("Enter a Number: "))))
lst1 = [int(item) for item in input("Enter the list items : ").split()]
print("Insertion Sort : ", iSort(lst1))
print("Bubble Sort : ", bSort(lst1))
print("Selection Sort : ", selSort(lst1))
srch = int(input("Enter an item to Search : "))
print("Linear Search - index : ", lSrch(lst1, srch))
print("Binary Search - index : ", bSrch(lst1, srch))



