'''
You have been given a vector/list 'ARR' consisting of ‘N’ integers. You are also given a positive integer ‘K’.

Let’s define a vector/list 'CONCAT' of size 'N * K' formed by concatenating 'ARR' ‘K’ times. For example, if 'ARR' = [0, -1, 2] and 'K' = 3, then 'CONCAT' is given by [0, -1, 2, 0, -1, 2, 0, -1, 2].

Your task is to find the maximum possible sum of any non-empty subarray (contagious) of 'CONCAT'.

Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T <= 100
1 <= N <= 10^4
1 <= K <= 10^4    
-10^5 <= ARR[i] <= 10^5

Time Limit: 1sec
Sample Input 1 :
2
2 3
1 3
3 2
1 -2 1
Sample Output 1 :
12
2
Sample Output 1 Explanation:
For the first test case, vector 'CONCAT' is obtained by concatenating vector [1, 3] three times. 
'CONCAT' = [1, 3, 1, 3, 1, 3]

The subarray with a maximum sum of 12 is [1, 3, 1, 3, 1, 3].


For the second test case, vector 'CONCAT' is obtained by concatenating vector [1, -2, 1] two times. 
'CONCAT' = [1, -2, 1, 1, -2, 1]

The subarray with a maximum sum of 2 is [1, 1].
Sample Input 2 :
1
2 3
-2 1 
Sample Output 2 :
1'''
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
print(result)       #(O/P: -1)

# Example usage:
arr = [1, 2, 3]
n = len(arr)
k = 2
result = maxSubSumKConcat(arr, n, k)
print(result)
#(O/p:   12)
