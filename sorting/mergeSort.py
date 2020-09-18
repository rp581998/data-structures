def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        leftHalf = arr[:mid] # 56,24,93,17
        rightHalf = arr[mid:] # 77,31,44,55,20
        mergeSort(leftHalf)
        mergeSort(rightHalf)
        i = j =  k = 0
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                arr[k] = leftHalf[i]
                i += 1
            else:
                arr[k] = rightHalf[j]
                j += 1
            k += 1
        while i < len(leftHalf):
            arr[k] = leftHalf[i]
            i += 1
            k += 1
        while j < len(rightHalf):
            arr[k] = rightHalf[j]
            j += 1
            k += 1

arr = [56,24,93,17,77,31,44,55,20]
mergeSort(arr)
print(arr)