'''
You have been given an array/list 'ARR' of integers. Your task is to find the second largest element present in the 'ARR'.

Note:
a) Duplicate elements may be present.

b) If no such element is present return -1.
Example:
Input: Given a sequence of five numbers 2, 4, 5, 6, 8.

Output:  6

Explanation:
In the given sequence of numbers, number 8 is the largest element, followed by number 6 which is the second-largest element. Hence we return number 6 which is the second-largest element in the sequence.
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T <= 100
1 <= N <= 5000
-10 ^ 9 <= 'SIZE' <= 10 ^ 9 

Where ‘T’ is the total number of test cases, ‘N’ denotes the number of elements in the array 
and ‘SIZE’ denotes the range of the elements in the array.

Time limit: 1 sec.
Sample Input 1:
2
6
12 1 35 10 34 1
5
10 10 10 10 10
Sample Output 1:
34
-1
Explanation of sample input 1:
Test case 1: In the given sequence of numbers, number 35 is the largest element, 
followed by number 34 which is the second-largest element. 
Hence we return number 34 which is the second-largest element in the sequence.

Test case 2: In the given sequence of numbers, number 10 is the largest element. 

However, since all the elements are the same, the second largest element does not exist. So, we return -1.
Sample Input 2:
1
6
7 8 8 1 4 3 
Sample Output 2:
7
Explanation of sample input 2:
In the given sequence of numbers, 8 exists two times and is the largest element, 
followed by 7 which is the second-largest element. Hence we return the number 7 as the second-largest element.'''
from os import *
from sys import *
from collections import *
from math import *

from sys import stdin
import sys

def findSecondLargest(arr):
    # Write your code here.
    if len(arr) < 2:
        return -1

    # Remove duplicates and sort the array in descending order
    unique_sorted_arr = sorted(set(arr), reverse=True)

    # If there is at least one unique element other than the largest one
    if len(unique_sorted_arr) > 1:
        return unique_sorted_arr[1]
    else:
        return -1




# Taking input using fast I/O.
def takeInput():
    n = int(input())

    sequenceOfNumbers = list(map(int, input().strip().split(" ")))

    return sequenceOfNumbers, n

# Main.
t = int(input())
while t:
    sequenceOfNumbers, n = takeInput()
    print(findSecondLargest(sequenceOfNumbers))
    t = t-1
