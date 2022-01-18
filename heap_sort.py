# n = heap size
def heapify(arr,n,i):
    largest = i
    # l = left, r = right 
    # two child of index i
    l = 2*i + 1
    r = 2*i + 2
    
    # checking if left child is greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l
    
    # checking if right child is greater than root    
    if r < n and arr[largest] < arr[r]:
        largest = r
    
    # change root if any of its child is greater    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr,n,largest)

def heap_sort(arr):
    n = len(arr)
    
    # to build heap
    for i in range(n//2 - 1,-1,-1):
        heapify(arr,n,i)
    
    # to extract elements    
    for i in range(n-1,0,-1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr,i,0)
        
arr = [12, 11, 13, 5, 6, 7,234,34,34,56,35342,2314,123,2,2]
heap_sort(arr)
print(arr)
