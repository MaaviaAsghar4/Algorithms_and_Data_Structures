arr = [-5, -10, 8, 20, 3, 8, -50, 39] 

def max_crossing_sum(arr,low,mid,high):
    _sum = 0
    left_sum = -100000000 # or -Inf
    right_sum = -100000000 # or -Inf
    max_left = 0
    max_right = 0
    for i in range(mid,low-1,-1): # low-1 to run it the first element in the list
        _sum += arr[i]
        if _sum > left_sum:
            left_sum = _sum
            max_left = i
    _sum = 0
    for j in range(mid+1,high+1): # high+1 to run it the last element in the list
        _sum += arr[j]
        if _sum > right_sum:
            right_sum = _sum
            max_right = j
    return (max_left,max_right,max(left_sum,right_sum,left_sum+right_sum))

def max_subarray(arr,low,high):
    if low == high:
        return (low,high,arr[low])
    else:
        mid = (low + high)//2
        (left_low,left_high,left_sum) = max_subarray(arr,low,mid)
        (right_low,right_high,right_sum) = max_subarray(arr,mid+1,high)
        (cross_low,cross_high,cross_sum) = max_crossing_sum(arr,low,mid,high)
    if (left_sum > right_sum and left_sum > cross_sum):
        return (left_low,left_high,left_sum)
    elif (right_sum > left_sum and right_sum > cross_sum):
        return (right_low,right_high,right_sum)
    else:
        return (cross_low,cross_high,cross_sum)
            
print(max_subarray(arr,0,len(arr)-1))
