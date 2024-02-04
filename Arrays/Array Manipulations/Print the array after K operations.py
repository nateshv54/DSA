'''
You are given an array 'ARR' consisting of 'N' integers and a non-negative integer 'K'. Consider an operation on the array as replacing every element 'ELE' of the array with 'MX - ELE', where 'MX' is the maximum element of the array. You need to return the updated array, given that this operation is performed on the array exactly 'K' number of times.

Note:

1. The array follows 0-based indexing.
2. Note that after each operation, the next operation will be performed on the updated array i.e the array obtained after the last operation.
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T <= 100
1 <= N <= 10^4
-10^9 <= ARR[i] <= 10^9
0 <= K <= 10^9

Time Limit: 1sec
Sample Input 1:
1
4 2
20 15 10 5
Sample Output 1:
15 10 5 0
Explanation for Sample Input 1:
The given array’s 0-based indexing is as follows:

In the first operation, maximum = 20.

20    15    10    5     
↓      ↓    ↓     ↓
0      5    10    15

These will be the array values, after one operation.

In the second operation,  maximum = 15.

0      5     10    15     
↓      ↓      ↓     ↓
15     10     5     0

Now the array to be returned is {15, 10, 5, 0}.
Sample Input 2:
1
4 3
0 0 9 18
Sample Output 2:
18 18 9 0  '''
from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, stdout


def printArrayAfterKOperations(arr, N, K):
    if K == 0:
        return arr

    soln = list()

    # Finding maximum element of the array.
    maxm = max(arr)  
    # Finding minimum element of the array.
    minm = min(arr)  

    # If K is odd, then all array will be transformed to maxm - Arr[i].
    if K & 1:
        for i in range(N):
            soln.append(maxm - arr[i])

    # Else if K is even, then all array will be transformed to minm - Arr[i].
    else:
        for i in range(N):
            soln.append(arr[i] - minm)

    return soln


# Taking input using fast I/0.
def takeInput():
    N, K = list(map(int, stdin.readline().strip().split(" ")))
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return N, K, arr


tc = int(input())
while tc > 0:
    N, K, arr = takeInput()
    sol = printArrayAfterKOperations(arr, N, K)
    for i in sol:
        stdout.write(str(i) + " ")
    stdout.write("\n")
    tc -= 1
