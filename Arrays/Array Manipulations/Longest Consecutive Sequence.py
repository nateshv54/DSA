'''
You are given an unsorted array/list 'ARR' of 'N' integers. Your task is to return the length of the longest consecutive sequence.

The consecutive sequence is in the form ['NUM', 'NUM' + 1, 'NUM' + 2, ..., 'NUM' + L] where 'NUM' is the starting integer of the sequence 
and 'L' + 1 is the length of the sequence.

Note:

If there are any duplicates in the given array we will count only one of them in the consecutive sequence.
For example-
For the given 'ARR' [9,5,4,9,10,10,6].

Output = 3
The longest consecutive sequence is [4,5,6].
Follow Up:
Can you solve this in O(N) time and O(N) space complexity?
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= T <= 10
1 <= N <= 10^5
-10^9 <= ARR[i] <= 10^9

Time Limit: 1 sec
Sample Input 1 :
1 
5
33 20 34 30 35
Sample Output 1 :
3
Explanation to Sample Input 1 :
The longest consecutive sequence is [33, 34, 35].
Sample Input 2 :
1
7
1 9 3 10 4 20 2    
Sample Output 2 :
4
Explanation to Sample Input 2 :
The consecutive sequence is in the form ['NUM', 'NUM' + 1, 'NUM' + 2,...,'NUM' + 'L']. 
So in the given array, the longest consecutive sequence is [1,2,3,4] where 'NUM' = 1 and 'L' = 3. 
And the length of the sequence will be 'L' + 1 = 4.'''

from math import *
from collections import *
from sys import *
from os import *

def lengthOfLongestConsecutiveSequence(arr, n):
    # Write your code here.
    if not arr:
        return 0
    
    # Create a set to store unique elements of the array
    num_set = set(arr)
    max_length = 0
    
    # Iterate through the array to find the start of each potential consecutive sequence
    for num in num_set:
        # Check if num is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            # Extend the consecutive sequence to the right
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)
    
    return max_length

# Driver code
if __name__ == "__main__":
    arr = [100, 4, 200, 1, 3, 2]
    n = len(arr)

    result = lengthOfLongestConsecutiveSequence(arr, n)
    
    print("Length of the longest consecutive sequence:", result)
