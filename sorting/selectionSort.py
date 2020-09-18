'''def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        minimum = i
        for j in range(i+1,n):
            if arr[j] < arr[minimum]:
                minimum = j
        swap(arr, minimum, i)
#        temp = arr[minimum]
#        arr[minimum] = arr[i]
#        arr[i] = temp
def swap(arr, x, y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp
'''
#                           OR USE THIS
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        minimum = i
        for j in range(i+1,n):
            if arr[j] < arr[minimum]:
                minimum = j
        temp = arr[minimum]
        arr[minimum] = arr[i]
        arr[i] = temp


arr = [10,9,15,1,5,2,6,3]
selectionSort(arr)
print('Sorted array: ')
print(arr)