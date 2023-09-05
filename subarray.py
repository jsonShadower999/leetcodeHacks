def find_subarray_with_given_sum(arr, sum):
    n = len(arr)
    curr_sum = arr[0]
    start = 0
    i = 1
    while i <= n:
        while curr_sum > sum and start < i-1:
            curr_sum = curr_sum - arr[start]
            start += 1
        if curr_sum == sum:
            return (start, i-1)
        if i < n:
            curr_sum = curr_sum + arr[i]
        i += 1
    return (-1, -1)
 
 
arr = [15, 2, 4, 8, 9, 5, 10, 23]
sum = 23
result = find_subarray_with_given_sum(arr, sum)
