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
    char_count = [0] * 128  
    i, j = 0, 0  
    distinct_count = 0  
    max_value = 0  

    while j < len(s):  
        if char_count[ord(s[j])] == 0:  
            distinct_count += 1  
        char_count[ord(s[j])] += 1  

        while distinct_count > k:  # Inner loop to adjust the window size if the distinct character count exceeds k.
            char_count[ord(s[i])] -= 1  # Decrement the count of the character at the start of the window.
            if char_count[ord(s[i])] == 0:
                distinct_count -= 1  # Decrement distinct_count if the count becomes zero.
            i += 1  # Move the start pointer to the next character.

        max_value = max(max_value, j - i + 1)  # Update max_value with the length of the current substring.
        j += 1  # Move the end pointer to the next character.

    return max_value  # Return the length of the longest substring with at most k distinct characters.

if __name__ == "__main__":
    S = input("Enter a String: ")
    k = int(input("Enter Number of Distinct characters: "))
    print(getLengthofLongestSubstring(S, k))
