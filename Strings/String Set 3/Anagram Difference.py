'''
You have been given two strings, let's say 'STR1' and 'STR2' of equal lengths.
 You are supposed to return the minimum number of manipulations required to make the two strings anagrams.
 
 Constraints :
1<= T <= 100
1<= N <= 5*10^3

Where 'N' is the length of strings 'STR1' and 'STR2'.

Time limit: 1 sec
Sample Input 1:
2
except
accept
buy
bye
Sample Output 1 :
2
1
Explanation Of Sample Output 1 :
In test case 1, we can change two character of  'STR1' i.e. {'e','x'} to {'a','c'} or we can change two character of  'STR2'
 i.e. {'a','c'} to {'e','x'}, to make string anagram. So the minimum number of manipulations to make 'STR1' and  'STR2' to 
 anagram string will be 2.

In test case 2, we can change one character of  'STR1' i.e. {'u'} to {'e'} or we can change one character of  'STR2' i.e.
 {'e'} to {'u'}, to make string anagram. So the minimum number of manipulations to make  'STR1' and 'STR2' to anagram string will be 1.

Sample Input 2:
2
mail
male
ninja
ninja
Sample Output 2 :
1
0
Explanation Of Sample Output 2 :
In test case 1, we can change one character of  'STR1' i.e. {'i'} to {'e'} or we can change one character of  'STR2' i.e.
 {'e'} to {'i'}, to make string anagram. So the minimum number of manipulations to make  'STR1' and  'STR2' to anagram string will be 1.

In test case 2, both strings are already anagram. So we do not need to do any manipulation. So the minimum number of manipulations
 to make  'STR1' and  'STR2' to anagram string will be 0.'''

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def getMinimumAnagramDifference(str1, str2):
    # Write your code here.
    char1=[0]*128
    for i in str1:
        char1[ord(i)]+=1
    for i in str2:
        char1[ord(i)]-=1
    count=0
    for i in range(128):
        if char1[i]>=1:
            count+=char1[i]
    return count
    
# Taking Input.
def takeInput():
    str1 = stdin.readline().strip()
    str2 = stdin.readline().strip()
    return str1, str2

# Main.
T = int(stdin.readline().strip())
for i in range(T):
    str1, str2 = takeInput()
    ans = getMinimumAnagramDifference(str1, str2)
    print(ans)