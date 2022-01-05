arr = [4,2,45,635,213,34,0,8]

def merge(arr,left_arr,right_arr):
    i = j = k = 0
    # comparing the value of two arrays and sorting it until all the elements are sorted
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j +=1
        k += 1
    # Checking if any element is left in first array
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    # Checking if any element is left in second array
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

def mergeSort(arr):
    # terminating condition for recursion
    if len(arr) > 1:
        # Finding mid of arr to split it into two equal arr
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        # Calling mergeSort recursively on newly created arrays
        mergeSort(left_arr)
        mergeSort(right_arr)
        # merging two arrays
        merge(arr,left_arr,right_arr)
    
mergeSort(arr)
print(arr)
