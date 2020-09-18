def quickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)
def partition(arr, low, high):
    pivot = low
    swap(arr, pivot, high)
    for i in range(low , high):
        if arr[i] <= arr[high]:
            swap(arr, i, low)
            low += 1
    swap(arr, low, high)
    return low

def swap(arr, x, y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp

arr= [5,4,6,8,1,9,2,0,3,7,10]
quickSort(arr, 0, len(arr)-1)
print(arr)
    