'''
You are given two versions numbers A and B as a string. 
Your task is to compare them and find out which one of them is a newer version.
Note:
There are no leading zeros in any of the strings except in the case of zero itself. 
Note that, the leading zeroes are not allowed even after a '.' ie: 121.005 is an invalid version, while 121.5 is an valid version.
For Example:
A = “1.23.45”, B = “1.23.456”

The first two parts of both the strings are the same i.e 1 and 23 and the third part of B is greater than the third part of A i.e.
 45 < 456, thus string B is the latest version.
 
 All the string A and B characters contain digits and dots only and both the strings are started and terminated by a digit.
Sample Input 1:
2
1.2.4
1.2.3
10.2.2
10.2.2
Sample Output 1:
1
0
Explanation for Sample Input 1:
For the first test case, the first two parts of both the strings are the same but the third part of the 1st version
 is bigger than the 2nd version. Hence our answer is 1

For the second test case, both the versions are identical here, so the answer will be 0.
Sample Input 2:
2
123.45
123
1.0.0
1
Sample output 2:
1
0
'''
from os import *
from sys import *
from collections import *
from math import *

def compareVersions(a, b):
    #Write your code here
    k = [int(w) for w in a.split(".")]
    l = [int(w) for w in b.split(".")]
    n = max(len(k), len(l))
    i = 0
    while i < n:
        k_comp = k[i] if i < len(k) else 0  # Consider missing components as 0
        l_comp = l[i] if i < len(l) else 0  # Consider missing components as 0
        
        if k_comp > l_comp:
            return 1
        elif k_comp < l_comp:
            return -1
        i += 1
    return 0  # a and b have the same version

# Example usage:
print(compareVersions("1.2.3", "1.2.3"))  # Output: 0
print(compareVersions("1.2.3", "1.2.4"))  # Output: -1
print(compareVersions("1.2.3", "1.2.2"))  # Output: 1

