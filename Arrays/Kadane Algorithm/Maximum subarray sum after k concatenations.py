from os import *
from sys import *
from collections import *
from math import *

def maxSubSumKConcat(arr, n, k):
    curr = 0
    max_sum = float('-inf')  # Initialize max_sum to negative infinity
    arr = arr * k

    for i in range(len(arr)):
        curr += arr[i]
        max_sum = max(max_sum, curr)
        
        if curr < 0:
            curr = 0

    return max_sum

#optimal method
def maxSubSumKConcat(arr, n, k):
    curr_max = 0
    max_sum = float('-inf')  # Initialize max_sum to negative infinity

    for i in range(n * min(k, 2)):  # Limit iterations to handle large k efficiently
        idx = i % n
        curr_max = max(arr[idx], curr_max + arr[idx])
        max_sum = max(max_sum, curr_max)

    # If max_sum is still negative, the entire array is negative, return the maximum element
    if max_sum < 0:
        return max(arr)

    # If k is greater than 2, the maximum subarray sum may span multiple repetitions
    if k > 2:
        max_sum += max(0, sum(arr)) * (k - 2)

    return max_sum

# Example usage:
arr = [-1, -2, -3, -4]
n = len(arr)
k = 3
result = maxSubSumKConcat(arr, n, k)
print(result)
