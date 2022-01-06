arr = [1,3,45,23,4535,546,67,34,43,234,1,3,45,23,4535,546,67,34,43,234,1,3,45,23,4535,546,67,34,43,234,1,3,45,23,4535,546,67,34,43,234,1,3,45,23,4535,546,67,34,43,234,1,3,45,23,4535,546,67,34,43,234,1,3,45,23,4535,546,67,34,43,234]
# merge arr
def merge(arr,left,right):
    i=j=k=0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[i]
        j += 1
        k += 1

# insertionSort
def insertionSort(arr):
    for j in range(1,len(arr)):
        key = arr[j]
        i = j -1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key

# mergeSort
def mergeSort(arr):
    if len(arr) > 1:
        # Running insertion sort when array length is less than 15
        if len(arr) < 15:
            insertionSort(arr)
        # Running merge sort when array length is more than 15
        else:
            mid = len(arr)//2
            left = arr[:mid]
            right = arr[mid:]
            mergeSort(left)
            mergeSort(right)
            merge(arr,left,right)
        
mergeSort(arr)
print(arr)
