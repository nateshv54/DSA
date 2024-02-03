'''
You are given an array of integers ARR[] of size N consisting of zeros and ones. You have to select a subset and flip bits of that subset. You have to return the count of maximum one’s that you can obtain by flipping chosen sub-array at most once.

A flip operation is one in which you turn 1 into 0 and 0 into 1.

For example:
If you are given an array {1, 1, 0, 0, 1} then you will have to return the count of maximum one’s you can obtain by flipping anyone chosen sub-array at most once, so here you will clearly choose sub-array from the index 2 to 3 and then flip it's bits. So, the final array comes out to be {1, 1, 1, 1, 1} which contains five ones and so you will return 5.
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T = 100
1 <= N <= 10^4
0 <= ARR[i] <= 1

Time Limit: 1 sec
Sample Input 1 :
3
5
1 0 0 1 0
4
1 1 1 0
5
0 0 1 0 0
Sample Output 1 :
4
4
4
Explanation For Sample Input 1:
For the first test case:
We can perform a flip operation in the range [1,2]. After the flip operation, the array is: 1 1 1 1 0
and so the answer will be 4

Similarly, in the second test case :
We can perform a flip operation in the range [3,3]. After the flip operation, the array is: 1 1 1 1 
and so the answer will be 4.

Finally for the third test case :
We can perform a flip operation in the range [0,4] 
After the flip operation, the array is: 1 1 0 1 1 
and so the answer will be 4
Sample Input 2 :
3
5
0 0 0 0 0
5
1 1 1 1 1
8
1 0 1 0 1 0 1 0
Sample Output 2 :
5
5
5
'''
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
