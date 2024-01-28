from os import *
from sys import *
from collections import *
from math import *

def flipBits(arr, n): 
    # Initialize the count of total ones
    total1 = 0
    
    # Initialize the maximum difference for any subarray
    max_val = 0
    
    # Initialize the current difference for the subarray being considered
    curr = 0
    
    # Loop through each element in the array
    for i in range(n):
        # Increment total1 if the current element is 1
        if arr[i] == 1:
            total1 += 1
        
        # Determine the value to be considered for finding the maximum sum
        val = 0
        if arr[i] == 1:
            val = -1
        else:
            val = 1
        
        # Update the current difference for the subarray
        curr = max(val, curr + val)
        
        # Update the overall maximum difference
        max_val = max(max_val, curr)

    # Ensure max_val is at least 0
    max_val = max(0, max_val)

    # Calculate the final result by adding total1 and max_val
    return total1 + max_val

# Example usage:
arr = [1, 0, 0, 1, 0]
n = len(arr)
result = flipBits(arr, n)
print(result)
