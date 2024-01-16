#Edit Distance
'''
Given two strings str1 and str2 of length M and N respectively and below operations that can be performed on str1. Find the minimum number of edits (operations) to convert ‘str1‘ into ‘str2‘.  

Operation 1 (INSERT): Insert any character before or after any index of str1
Operation 2 (REMOVE): Remove a character of str1
Operation 3 (Replace): Replace a character at any index of str1 with some other character.
Note: All of the above operations are of equal cost. 

'''

def editdistance(s1,s2,m,n):
    if m==0 or n==0:
        return m+n
    if s1[m-1] == s2[n-1]:
        return editdistance(s1,s2,m-1,n-1)
    
    return 1+min(editdistance(s1,s2,m,n-1),
                 editdistance(s1,s2,m-1,n),
                 (editdistance(s1,s2,m-1,n-1)))

m='sunday'
n='saturday'
print(editdistance(m,n,len(m),len(n)))