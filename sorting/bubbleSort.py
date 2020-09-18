'''def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

arr = [10,9,15,1,5,2,6,3]
bubbleSort(arr)
print('Sorted array: ')
for i in range(len(arr)):
    print(arr[i])
'''
#                       OR use this           
'''
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)
def swap(arr, x, y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp
'''
#                       OR use this,swap from last

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1,i,-1):
            if arr[j] < arr[j-1]:
                swap(arr, j, j-1)
def swap(arr, x, y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp
arr = [10,9,15,1,5,2,6,3]
bubbleSort(arr)
print('Sorted array: ')
print(arr)