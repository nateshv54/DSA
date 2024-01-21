#Longest_substring_with_K_distinct characters
'''
You are a String S(lowercase) and integer K(+ve).
A substring of S is good if it contains at most  K distinct characters.
Return the max_size of substring of string S.

Input:-
S="bacda"
k=3

Explanation:-
The possible substrings are:
1. bacd
2. acda
3. bac
4. acd
5. cda
  '''
from os import *
from sys import *
from collections import *
from math import *

def getLengthofLongestSubstring(s, k):

    # Write your code here.
    i=0
    j=0
    max_value=0
    while j<len(s):
        length=len(set(s[i:j+1]))
        if length<=k:
            max_value=max(max_value,len(s[i:j+1]))
            j+=1
        else:
            i+=1
            j=i
    return max_value

if __name__=="__main__":
    S=input("Enter a String: ")
    k=int(input("Enter Number of Distinct characters: "))
    print(getLengthofLongestSubstring(S,k))