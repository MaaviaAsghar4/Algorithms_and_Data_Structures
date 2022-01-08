# brute force method for maximum subarray
def max_subarray_brute(arr):
    total, start , end = 0, 0, 0
    for i in range(0,len(arr)):
        sum_ = 0
        for j in range(i,len(arr)):
            sum_ += arr[j]
            if total < sum_:
                total, start, end = sum_, i, j
                
    return [total,start,end]
            
    
print(max_subarray_brute([-5, -10, 8, 20, 3, 8, -50, 39]))
