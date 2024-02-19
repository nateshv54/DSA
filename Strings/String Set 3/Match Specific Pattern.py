'''
Problem statement
Ninja has given you a list of WORDS and a PATTERN string. Your task is to find all such words in the list which match the given pattern. A valid match is found if and only if every character in the pattern is uniquely mapped to a character in a word.

Example:

Let the list of words be {cod, zcz} and the pattern be ‘nin’.
For each word in the list, we will check whether the word matches the pattern or not:

For the word ‘cod’:
Letter ‘n’ in the pattern maps to letter ‘c’ in the word.
Letter ‘i’ in the pattern maps to letter ‘o’ in the word.
Letter ‘n’ in the pattern maps to letter ‘d’ in the word.

As the same letter ‘n’ in the pattern, maps to two different letters ‘c’ and ‘d’ in the word. Hence, ‘cod’ is not a valid match.

For the word 'zcz':
Letter ‘n’ in the pattern maps to letter ‘z’ in the word.
Letter ‘i’ in the pattern maps to letter ‘c’ in the word.
Letter ‘n’ in the pattern maps to letter ‘z’ in the word.

As every letter in the pattern maps uniquely to a corresponding letter in the word. Hence 'zcz' is a valid match.
Sample Input 1:
2
2
cdd pcm
foo
3
abcd km qst
pqr
Sample Output 1:
cdd 
qst 
Explanation 1:
For the first test case, the list of words is {cdd, pcm} and the pattern is 'foo'. 

For the word 'cdd': 
The letters ‘f’, ‘o’, ‘o’ of the pattern, map to letters ‘c’, ‘d’, ‘d’ of the word respectively. As every letter in the pattern maps uniquely to a corresponding letter in the word. Hence, it is a valid match.

For the word 'pcm': 
The letters ‘f’, ‘o’, ‘o’ of the pattern map to letters ‘p’, ‘c’, ‘m’ of the word respectively. As the same letter ‘o’, in the pattern, maps to two different letters ‘c’ and ‘m’ in the word. Hence, 'pcm' is not a valid match.

For the second test case, the list of words is {abcd, km, qst} and the pattern is 'pqr'.

For the word 'abcd': 
The letters ‘p’, ‘q’, ‘r’ of the pattern map to letters ‘a’, ‘b’, ‘c’ of the word respectively. But, there is no character in the pattern which maps to the letter ‘d’ in the word. Hence, it is not a valid match.

For the word 'km':
The letters ‘p’, ‘q’ of the pattern, map to letters ‘k’, ‘m’ of the word respectively. But. there is no character in the word which maps to the letter ‘r’ in the pattern. Hence, it is not a valid match. 

For the word 'qst': 
The letters ‘p’, ‘q’, ‘r’ of the pattern map to letters ‘q’, ‘s’, ‘t’ of the word respectively. As every letter in the pattern maps uniquely to a corresponding letter in the word. Hence, it is a valid match.
Sample Input 2:
2
5
aaaa abcd code toma zedi
pqrs
6
adff coding ejqq fstt ggnn ninja
lmnn
Sample Output 2:
abcd code toma zedi
adff ejqq fstt
Sample Input 3:
2
3
#h#@# AmAka &t&y&   
%R%s%
1
A
B
Sample Output 3:
#h#@# &t&y&  
A'''






from os import *
from sys import *
from collections import *
from math import *

def generateHash(str):

    # Maintain a HashMap
    mp = {}

    # Create a varible hash, which will store the hash for a given word
    hash = ''

    counter = 1

    for i in range(len(str)):

        ch = str[i]

        if (ch not in mp.keys()):

            # Found a distinct character
            mp[ch] = counter
            counter += 1

        converted_num = '% s' % mp[ch]
        hash = hash + converted_num

    # Return the variable hash
    return hash

def matchSpecificPattern(words, n, pattern):

    # Create an array to store all valid words
    ans = []

    hashPattern = generateHash(pattern)

    # Iterate over all the words
    for i in range(n):

        word = words[i]

        if (len(word) == len(pattern)):
            
            hashWord = generateHash(word)

            if (hashWord == hashPattern):

                # Word matches the pattern
                ans.append(word)

    # Return the array answer
    return ans

# Sample list of words
words = ["abc", "def", "ghi", "jkl", "mno", "pqr", "stu"]

# Pattern to match
pattern = "xyz"

# Get the list of words that match the pattern
matched_words = matchSpecificPattern(words, len(words), pattern)

# Print the matched words
print("Words that match the pattern:", matched_words)
