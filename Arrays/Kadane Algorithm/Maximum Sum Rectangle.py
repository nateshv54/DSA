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
