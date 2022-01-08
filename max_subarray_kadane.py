def max_subarray(arr):
    _sum = 0
    max_so_far = 0
    last_index = 0
    for i in range(0,len(arr)):
        max_so_far += arr[i]
        # Dropping elements when max_so_far < 0
        if max_so_far < 0:
            max_so_far = 0
        elif (_sum < max_so_far):
            _sum = max_so_far
            last_index = i
    return [_sum,last_index]
print(max_subarray([-5, -10, 8, 20, 3, 8, -50, 39]))
