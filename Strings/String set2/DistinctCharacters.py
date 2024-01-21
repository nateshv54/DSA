#O(n*n)
def non_repeatingCharacterCount(s):
    s=s.lower()
    for i in range(0,len(s)):
        flag=0
        for j in range(0,len(s)):
            if(s[i]==s[j] and i!=j):
                flag=1
                break
        if flag==0:
            print(s[i],end=" ")

s=input("Enter string value: ")
non_repeatingCharacterCount(s)

'''
Enter string value: geeksforgeeks
f o r
'''