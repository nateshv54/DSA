'''
You have been given an integer array/list 'ARR' of size 'N'. Write a solution to check if it could become non-decreasing by modifying at most 1 element.

We define an array as non-decreasing, if ARR[i] <= ARR[i + 1] holds for every i (0-based) such that (0 <= i <= N - 2).

Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= T <= 50
1 <= N <= 10 ^ 4
- 10 ^ 9 <= ARR[i] <= 10 ^ 9

Where 'N' is the size of the given array/list.
And, ARR[i] denotes the i-th element in the array/list 'ARR'.

Time Limit: 1sec
Sample Input 1 :
2
3
8 4 6
3
8 4 2
Sample Output 1 :
true
false
Explanation to Sample Input 1 :
For Test Case 1 we can have a possible non-decreasing array : 2 4 6
Where only the element at index 0 has been modified.

For Test Case 2 there is no possible way to make the array non-decreasing by modifying at most 1 element.
Sample Input 2 :
2
6
-2 7 -1 0 1 2
5
-10 10 0 10 3
Sample Output 2 :
true
false
Explanation to Sample Input 2 :
For Test Case 1 we can have a possible non-decreasing array : -2 -2 -1 0 1 2
Where only the element at index 1 has been modified

For Test Case 2 there is no possible way to make the array non-decreasing by modifying at most 1 element.'''
from os import *
from sys import *
from collections import *
from math import *

def isPossible(arr, n):
    
    notInOrderIndex = -1
    
    for i in range(n-1):
        
        if(arr[i] > arr[i+1]):
            
            '''
                If more than 1 Index is not in non-decreasing
                order then we can return false.
            '''
            if (notInOrderIndex != -1):
                
                return False
            
            notInOrderIndex = i
    
    '''
        If Everyone is in Order OR Only 
        First Number is not in Order OR Only Last
        number is not in Order.
    '''
    if (notInOrderIndex == -1 or notInOrderIndex == 0 or notInOrderIndex == n - 2):
        return True
      
    '''
        If we can change arr[notInOrderIndex]
        to be between arr[notInOrderIndex - 1]
        and arr[notInOrderIndex + 1].   
    '''
    if (arr[notInOrderIndex - 1] <= arr[notInOrderIndex + 1]):
        return True
    
    '''
        If we can change arr[notInOrderIndex + 1]
        to be between arr[notInOrderIndex]
        and arr[notInOrderIndex + 2].  
    '''
    if (arr[notInOrderIndex] <= arr[notInOrderIndex + 2]):
        return True
        
    '''
        If there is no way to make the array non-decreasing
        by modifying at most 1 element.
    '''
    return False

def main():
    # Test case 1
    arr1 = [1, 2, 3, 4, 5]
    n1 = len(arr1)
    print(isPossible(arr1, n1))  # Expected output: True

    # Test case 2
    arr2 = [1, 3, 2, 4, 5]
    n2 = len(arr2)
    print(isPossible(arr2, n2))  # Expected output: True

    # Test case 3
    arr3 = [1, 2, 5, 4, 3]
    n3 = len(arr3)
    print(isPossible(arr3, n3))  # Expected output: False

    # Test case 4
    arr4 = [5, 4, 3, 2, 1]
    n4 = len(arr4)
    print(isPossible(arr4, n4))  # Expected output: True

if __name__ == "__main__":
    main()

