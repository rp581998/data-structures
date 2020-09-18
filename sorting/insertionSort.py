def insertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        minimum = arr[i]
        k = i
        while minimum < arr[k-1] and k > 0:
            arr[k] = arr[k-1]
            k -= 1
        arr[k] = minimum

arr = [56,24,93,17,77,31,44,55,20]
insertionSort(arr)
print(arr)
