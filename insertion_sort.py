def insertionSort(arr):
  # Setting index = 1 as the first key to compare it to other values
    for j in range(1,len(arr)):
        key = arr[j]
        i = j - 1
        # moving the key to the sorted position (e.g. moving all values smaller than key before key)
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
        # setting key in the sorted position
        arr[i+1] = key
    return arr

print(insertionSort([1,0,234,65,234,4,76,678])) # prints ([1, 0, 4, 65, 76, 234, 234, 678])
