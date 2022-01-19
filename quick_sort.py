# function to return partion index
def partion_index(arr,low,high):
    pivot_index = low
    pivot = arr[pivot_index]
    # to swap low and high elements until the element is in sorted position
    while low < high:
      # find index of element smaller than pivot
        while low < len(arr) and arr[low] <= pivot:
            low += 1
      # find index of element larget than pivot      
        while arr[high] > pivot:
            high -= 1
      # swap low and high      
        if low < high:
            arr[low],arr[high] = arr[high],arr[low]
    # put the element on its correctly sorted place        
    arr[high],arr[pivot_index] = arr[pivot_index], arr[high]
    return high

def quick_sort(arr,low,high):
    if low < high:
        p = partion_index(arr,low,high)
        quick_sort(arr,low,p-1)
        quick_sort(arr,p+1,high)
        
        
arr = [1,23,34,45,21,34,3,543,34,23,21,34,43,5,787,645,5]
quick_sort(arr,0,len(arr)-1)
print(arr)
