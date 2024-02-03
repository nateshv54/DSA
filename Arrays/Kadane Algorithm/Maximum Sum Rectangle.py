'''
You are given a matrix ‘ARR’ with ‘N’ rows and ‘M’ columns. Your task is to find the maximum sum rectangle in the matrix.

Maximum sum rectangle is a rectangle with the maximum value for the sum of integers present within its boundary, considering all the rectangles that can be formed from the elements of that matrix.

For Example
Consider following matrix:

The rectangle (1,1) to (3,3) is the rectangle with the maximum sum, i.e. 29.

Detailed explanation ( Input/output format, Notes, Images )
Constraints
 1 <= T <= 10
 1 <= M, N <= 75
 -10^5 <= ARR[i][j] <= 10^5

Time Limit: 1 sec
Sample Input 1
2
1 2
-1 1
2 2
-1 1
2 2
Sample Output 1
1
4
Explanation of Input 1
The maximum sum rectangle corresponding to the first test case is-

The maximum sum rectangle corresponding to the second test case is-

Sample Input 2
1
4 5
1 2 -1 -4 -20
-8 -3  4 2 1
3  8 10 1 3
-4 -1 1 7 -6
Sample Output 2
29'''

from os import *
from sys import *
from collections import *
from math import *

def maxSumRectangle(arr, n, m):

    def maxSumSubarray(row):
        maxEndingHere = 0
        maxSoFar = float('-inf')

        for element in row:
            maxEndingHere = max(element, maxEndingHere + element)
            maxSoFar = max(maxSoFar, maxEndingHere)

        return maxSoFar

    maxSum = float('-inf')

    # Iterate through all possible pairs of rows (i, j)
    for i in range(n):
        tempRow = [0] * m

        for j in range(i, n):
            # Update tempRow to store the sum of elements in each column for the current pair of rows
            for k in range(m):
                tempRow[k] += arr[j][k]

            # Find the maximum sum subarray in the tempRow
            currentMaxSum = maxSumSubarray(tempRow)

            # Update maxSum if the currentMaxSum is greater
            maxSum = max(maxSum, currentMaxSum)

    return maxSum


# Driver Code
t = int(input("Enter the number of test cases: "))
for _ in range(t):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # Call the function and print the result
    result = maxSumRectangle(arr, n, m)
    print(result)
