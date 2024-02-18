'''
Problem statement
You have been given an Encrypted String where repetitions of substrings are represented as substring followed by the count of substrings.

Example: String "aabbbcdcdcd" will be encrypted as "a2b3cd3".
You need to find the 'K'th character of Decrypted String. Decrypted String would have 1-based indexing.

Note :

Input string will always be lowercase characters without any spaces.

If the count of a substring is 1 then also it will be followed by Integer '1'.
Example: "aabcdee" will be Encrypted as "a2bcd1e2"
This means it's guaranteed that each substring is followed by some Integer.

Also, the frequency of encrypted substring can be of more than one digit. For example, in "ab12c3", ab is repeated 12 times. No leading 0 is present in the frequency of substring.

The frequency of a repeated substring can also be in parts.
Example: "aaaabbbb" can also have "a2a2b3b1" as Encrypted String.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1 :
a2b3cd3
8
Sample Output 1 :
c
 Explanation to Sample Input 1 :
S = "a2b3cd3"
Decrypted String of S = "aabbbcdcdcd"
According to 1-based indexing for S, the 8th character is 'c'.
Sample Input 2 :
ab12c3
20
Sample Output 2 :
b
 Explanation to Sample Input 2 :
S = "ab12c3"
Decrypted String of S = "ababababababababababababccc"
So 20th character is 'b'.'''


from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def kThCharaterOfDecryptedString(s, k) :

    #  Length of the Encrypted String.
    n = len(s)
    i = 0
    
    while (i < n) :
    
        j = i
        substringLength = 0
        freqOfSubstring = 0

        # Find the length of substring by traversing the string until no digit is found.
        while (j < n and (s[j].islower())) :
        
            j += 1
            substringLength += 1
        

        # Find the frequency of preceding substring.
        while (j < n and (s[j].isdigit())) :
        
            freqOfSubstring = freqOfSubstring * 10 + (ord(s[j]) - ord('0')) 
            j += 1
        

        # Find length of the resultant length of the repeated substring.
        resultantLength = freqOfSubstring * substringLength

        if (k > resultantLength) :
        
            '''
                If length of the repeated substring is less than
                'k' then required character is present in later
                substring. Subtract the length of repeated
                substring from 'k' to keep account of number of
                characters required to be visited.
            '''

            k -= resultantLength
            i = j
        
        else :
        
            '''
                If length of repeated substring is
                more or equal to 'k' then required
                character lies in current substring.
            '''

            k -= 1
            k %= substringLength
            kThChar = s[i + k]
            break
    
    return kThChar

#taking inpit using fast I/O
def takeInput() :
	
    str1 = input().strip()
    k = int(input().strip())

    return str1, k

#main
str1, k = takeInput()
print(kThCharaterOfDecryptedString(str1, k))