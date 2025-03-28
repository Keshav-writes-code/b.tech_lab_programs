def display(arr):
    # Function to display elements of an array
    print(", ".join(map(str, arr)))

def insertion_sort(arr):
    # Function to perform insertion sort on the array
    for i in range(1, len(arr)):
        key, j = arr[i], i-1
        # Move elements greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j+1], j = arr[j], j-1
        arr[j+1] = key
    return arr

def bubble_sort(arr):
    # Function to perform bubble sort on the array
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

unsorted_arr = []
i = 1
while True:
    val = input(f"Enter Value {i} (press Enter to finish): ")
    if not val:
        break
    unsorted_arr.append(int(val))
    i += 1

print("\nUnsorted Array:")
display(unsorted_arr)

print("\n\n1. Insertion Sort\n2. Bubble Sort\nChoose a Sorting Algo: ", end="")
choice = int(input())
sorted_arr = insertion_sort(unsorted_arr) if choice == 1 else bubble_sort(unsorted_arr)

print("\n\nSorted Array:")
display(sorted_arr)
