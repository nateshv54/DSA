'''
Problem statement
You have been given two strings A and B consisting of lower case English letters. The task is to count the minimum number of pre-processing moves on the string A required to make it equal to string B after applying below operations:

1. Choose any index i (0 <= i < n) and swap characters a[i]  and b[i].
2. Choose any index i (0 <= i < n) and swap characters a[i]  and a[n-i-1] .
3. Choose any index i (0 <= i < n) and swap characters b[i]  and b[n-i-1] .
In one preprocess move, you can replace a character in A with any other character of the English alphabet.

Note:
1. The number of changes you make after the preprocess move does not matter.
2. You cannot apply to preprocess moves to the String B or make any preprocess moves after the first change is made.
Sample Input 1:
2
abacaba
bacabaa
zcabd
dbacz
Sample Output 1:
4
0
Explanation of Sample Input 1:
For the first test case, preprocess moves are as follows: A[0] = ‘b’, A[2] = ‘c’, A[3] = ‘a’ and A[4] = ‘b’. Afterwards, A = ‘“bbcabba”. Then we can obtain equal strings by the following sequence of changes: swap(A[2], B[2]) and swap(A[2], A[6]). There is no way to use fewer than 4 preprocess moves before a sequence of changes to make strings equal, so the answer in this test case is 4.

For the second test case, no preprocess moves are required. We can use the following sequence of changes to make A and B equal: swap(B[1], B[5]), swap(A[2], A[4]).
Sample Input 2:
3
zxyyxzx
zyzyxyy
jfhjfl
jhkkjs
abcd
abcde
Sample Output 2:
3
4
-1'''

from os import *
from sys import *
from collections import *
from math import *

import sys


def minimumOperations(a, b):

    if len(a) != len(b):
        return -1

    # Length of the given string.
    n = len(a)

    # To store the required answer.
    count = 0

    # Run a loop upto 'n'/2.
    for i in range(n//2):

        # To store frequency of 4 characters in the ith group.
        group = OrderedDict()

        group[a[i]] = group.get(a[i], 0) + 1
        group[a[n - i - 1]] = group.get(a[n - i - 1], 0) + 1
        group[b[i]] = group.get(b[i], 0) + 1
        group[b[n - i - 1]] = group.get(b[n - i - 1], 0) + 1

        size = len(group)

        # All four characters are distinct.
        if (size == 4):
            count += 2

        # Group contains three distinct characters.
        elif (size ==3):
            # Replace both characters of String 'a'.
            if (a[i] == a[n - i - 1]):
                count += 2
            else:
                count += 1

        # Group contains two distinct characters.
        elif (size == 2):
            #  Replace one character of String 'a'.
            if (group.get(a[i]) != 2):
                count += 1

    #  If 'n' is odd.
    if (n % 2 == 1 and a[n // 2] != b[n // 2]):
        count += 1

    return count



# Main.
t = int(input().strip())
for i in range(t):
    str_a = input().strip()
    str_b = input().strip()
    print(minimumOperations(str_a, str_b))
