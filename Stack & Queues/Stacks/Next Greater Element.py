"""
    Problem Statement: Finding Next Greater Element
    
    You are given an array of integers called `arr`. For each element in the array, you need to find the Next Greater Element (NGE),
    which is the first element on the right side of the current element that is greater than the current element. If there is no greater
    element to the right, consider the NGE as -1.

    Write a function `nextGreaterElement` that takes two parameters:
    - `arr`: a list of integers (1 <= length of arr <= 10^5)
    - `n`: an integer representing the size of the array `arr`

    The function should return a list containing the NGE for each element in the input array. If there is no greater element to the right,
    the corresponding element in the result list should be -1.

    Example:
    arr = [1, 5, 3, 4, 2]
    n = 5
    result = nextGreaterElement(arr, n)
    # Output: [5, -1, 4, -1, -1]

    In the given example, the NGE for the first element (1) is 5, for the second element (5) there is no greater element to the right (-1),
    for the third element (3) the NGE is 4, and so on.

    Note:
    - You are expected to solve this problem with a time complexity of O(n).
"""

from typing import List



def nextGreaterElement(arr: List[int], n: int) -> List[int]:
    stack = []
    result = [-1] * n  # Initialize the result list with -1

    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            result[stack.pop()] = arr[i]
        
        stack.append(i)

    return result

# Example usage:
# Sample Input 1:
arr1 = [1, 5, 3, 4, 2]
n1 = len(arr1)
output1 = nextGreaterElement(arr1, n1)
print("Output 1:", output1)
# Expected Output: [5, -1, 4, -1, -1]

# Sample Input 2:
arr2 = [5, 6, 5, 2, 8]
n2 = len(arr2)
output2 = nextGreaterElement(arr2, n2)
print("Output 2:", output2)
# Expected Output: [-1, -1, -1, -1, -1]


